from django.shortcuts import render
from os import path
from .forms import UploadForm

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
        uploadform = UploadForm(request.POST, request.FILES)
        if uploadform.is_valid():
            uf = request.FILES['file']
            fpath = path.join(APP_DIR + '/temp', str(uf))
            with open(fpath, 'wb+') as f:
                for chunk in uf.chunks():
                    f.write(chunk)
            return render(request, 'upload/upload.html', {'form': uploadform})
    uploadform = UploadForm()
    return render(request, 'upload/upload.html', {'form': uploadform})
