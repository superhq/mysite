from django.shortcuts import render
from .forms import CalForm

def cal(request):
    if request.method == 'post':
        return render(request, 'photo_collector/cal.html')
    else:
        calform = CalForm()
        return render(request, 'photo_collector/cal.html', {'calform': calform})
