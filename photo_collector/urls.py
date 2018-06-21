from django.urls import path

from . import views
app_name = 'photo_collector'
urlpatterns = [
    path('cal', views.cal, name='cal'),
]
