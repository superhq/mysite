# coding:utf-8
from django.shortcuts import render,reverse
from django.http import StreamingHttpResponse, HttpResponseRedirect
from os import path, walk
from .forms import UploadForm
from urllib.parse import unquote
import chardet
APP_DIR = path.dirname(path.abspath(__file__))


# def upload(request):
#     print(path.abspath(__file__))
#     if request.method == 'POST':
#         uf = request.FILES['uploadFile']
#         fpath = path.join(APP_DIR + '/temp', str(uf))
#         with open(fpath, 'wb+') as f:
#             for chunk in uf.chunks():
#                 f.write(chunk)
#     return render(request, 'upload/upload.html', {'message': 'upload'})


def upload(request):
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            temp_files = request.FILES.getlist('file')
            for temp in temp_files:
                out_path = path.join(APP_DIR + '/temp', str(temp))
                with open(out_path, 'wb+') as out:
                    for chunk in temp.chunks():
                        out.write(chunk)
            #return render(request, 'upload/upload.html', {'form': upload_form})
            return HttpResponseRedirect(reverse('upload:download'))
    upload_form = UploadForm()
    return render(request, 'upload/upload.html', {'form': upload_form})


#在chrome浏览器中，下载中文名的文件有问题；在ie中正常
def download(request, file=None):
    def read_file(filename, chunk_size=512):
        with open(filename, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    temp_path = path.join(APP_DIR, 'temp')
    if file:
        full_path = path.join(temp_path, file)
        response = StreamingHttpResponse(read_file(full_path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file)
        return response


    files = []
    for (root, dirs, tmp) in walk(temp_path):
        files = files + tmp
    #files = [path.join(temp_path,i) for i in files]
    return render(request, 'upload/download.html', {'files': files})
