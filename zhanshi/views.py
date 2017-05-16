#-*_ coding:utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'zhanshi/index.html')
def activity(request):
    return render(request,'zhanshi/activity.html')
def topicdistribution(request):
    return render(request,'zhanshi/topicdistribution.html')
