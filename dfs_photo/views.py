from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from dfsopensdk.protocol import *
from dfsopensdk.opensdk import *
from mysite import settings
import configparser
from os import path
from django.core.mail import send_mail, get_connection
from .forms import UploadForm, ContactForm
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


def thanks(request):
    return render(request, 'dfs_photo/thanks.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            message = '{}发送了消息：{}'.format(cd['name'], cd['message'])
            send_mail(
                cd['subject'],
                message,
                'test@test.com',
                ['hongqun@test.com'],
                connection=con
            )
            return HttpResponseRedirect(reverse('dfs_photo:thanks'))
    else:
        form = ContactForm(
            initial={'subject': 'This is a good website'}
        )
    return render(request, 'dfs_photo/contract.html', {'form': form})
