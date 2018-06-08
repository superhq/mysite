from django.shortcuts import render
from os import path, walk
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
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            temp_files = request.FILES.getlist('file')
            for temp in temp_files:
                out_path = path.join(APP_DIR + '/temp', str(temp))
                with open(out_path, 'wb+') as out:
                    for chunk in temp.chunks():
                        out.write(chunk)
            return render(request, 'upload/upload.html', {'form': upload_form})
    upload_form = UploadForm()
    return render(request, 'upload/upload.html', {'form': upload_form})


def download(request):
    temp_path = path.join(APP_DIR, 'temp')
    files = []
    for (root, dirs, tmp) in walk(temp_path):
        files = files + tmp

    return render(request, 'upload/download.html', {'files': files})
