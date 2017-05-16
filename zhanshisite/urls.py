#-*- coding:utf8 -*- 
"""zhanshisite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#项目的URLconf，对应网页URL的前部分
from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('zhanshi.urls')),
]
from django.conf import settings

if settings.DEBUG:   
    #自己指定静态文件夹,想为静态文件分配多个不同的网址时，可能会用上这个
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
