#-*- coding:utf-8 -*-
from . import views
from django.conf.urls import url
#应用的URLconf,对应网页url后半部分
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^activity',views.activity,name='activity'),
    url(r'^topic',views.topicdistribution,name='topic')
]
