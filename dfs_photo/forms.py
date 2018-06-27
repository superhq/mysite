from django import forms


class UploadForm(forms.Form):
    file = forms.FileField(label='要上传的文件', widget=forms.ClearableFileInput(attrs={'multiple': True}))


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='主题')
    name = forms.CharField(max_length=20,min_length=2, label="姓名")
    message = forms.CharField(widget=forms.Textarea, min_length=4, label='内容')

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('消息长度不够')
        else:
            return message

