from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def insert_topic(request):
    TO=TopicForm()
    d={'to':TO}
    
    if request.method=='POST':
        TPF=TopicForm(request.POST)
        if TPF.is_valid():
            TPF.save()
            return HttpResponse('topic is insetrted sucessfully')
    return render(request,'insert_topic.html',d)
def insert_webpage(request):
    WO=WebpageForm()
    d={'wo':WO}
    
    if request.method=='POST':
        TPF=WebpageForm(request.POST)
        if TPF.is_valid():
            TPF.save()
            return HttpResponse('webpage is insetrted sucessfully')
    return render(request,'insert_webpage.html',d)
def insert_accessrec(request):
    AO=AccessrecForm()
    d={'ao':AO}
    
    if request.method=='POST':
        TPF=AccessrecForm(request.POST)
        if TPF.is_valid():
            TPF.save()
            return HttpResponse('accessrecord is insetrted sucessfully')
    return render(request,'insert_accessrec.html',d)
    
    
    
    
