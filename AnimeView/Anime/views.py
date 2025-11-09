from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader
from .models import Anime

def home(request):
    Data=Anime.objects.all()
    temp=loader.get_template('Index.html')
    context={
        'test':Data
    }
    return HttpResponse(temp.render(context,request))

def anime(request,id):
    temp=loader.get_template("Test.html")
    return HttpResponse(temp.render())

def insert (request):
    return HttpResponse("Hello")
