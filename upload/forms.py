from django import forms


class UploadForm(forms.Form):
    file = forms.FileField(label='要上传的文件')
