from django.contrib import admin
from django.urls import path
from AppCoder.views import *
urlpatterns = [
    path('',home, name= "home"),
    path('group/',group, name = "group"),
    path('post/',post, name= "post"),
    path('usuario/', user, name= "user"),
    path('searchPost', search_post, name = "searchPost")
]