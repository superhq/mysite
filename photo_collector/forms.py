from django import forms


class CalForm(forms.Form):
    path = forms.FileField()
