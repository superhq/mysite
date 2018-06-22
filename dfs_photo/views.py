from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from dfsopensdk.protocol import *
from dfsopensdk.opensdk import *
from mysite import settings
import configparser
from os import path
from .forms import UploadForm
APP_DIR = path.dirname(path.abspath(__file__))
TMP = path.join(APP_DIR, 'temp')


def login(request):
    cnf = configparser.ConfigParser()
    cnf.read(settings.DFS_CNF)
    address = cnf.get('ADDRESS','SERVER')
    return HttpResponse(address)


def create(request):
    opt = SDK('192.168.0.61', 8443)
    opt.login('hongqun', 'sync', '123456', 'sunrun')
    ret = opt.mkdir(Classify.USER, '/照片')
    opt.logout()
    return HttpResponse('Create user folder success,%s'%(ret,))


def index(request):
    return HttpResponse('Success')


def upload(request):
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            temp_files = request.FILES.getlist('file')
            opt = SDK('192.168.0.61', 8443)
            opt.login('hongqun', 'sync', '123456', 'sunrun')
            for temp in temp_files:
                out_path = path.join(APP_DIR + '/temp', str(temp))
                with open(out_path, 'wb+') as out:
                    for chunk in temp.chunks():
                        out.write(chunk)
                opt.upload(out_path, '/照片', Classify.USER)
            opt.logout()

            return HttpResponseRedirect(reverse('dfs_photo:index'))
    upload_form = UploadForm()
    return render(request, 'dfs_photo/upload.html', {'form': upload_form})
