from django.urls import path
from . import views
app_name = 'dfs_photo'
urlpatterns = [
    path('create', views.create, name='create'),
    path('login', views.login, name='login'),
    path('upload', views.upload, name='upload'),
    path('index', views.index, name='index')
    ]
