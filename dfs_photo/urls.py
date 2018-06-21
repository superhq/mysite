from django.urls import path
from . import views
app_name = 'dfs_photo'
urlpatterns = [
    path('create',views.create,),
    path('login',views.login)
        ]