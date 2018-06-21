from django.shortcuts import render
from django.http import HttpResponse
from dfsopensdk.protocol import *
from dfsopensdk.opensdk import *
from mysite import settings
import configparser
# Create your views here.


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
