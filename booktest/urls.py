# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$',views.index),
    url(r'^myexp$',views.MyExp),
    url(r'^uploadPic$', views.uploadPic),
    url(r'^uploadHandle$', views.uploadHandle),
    url(r'^herolist/(\d+)$', views.herolist),
    url(r'^area$', views.area),
    url(r'^area/(\d+)$', views.area2),
]
