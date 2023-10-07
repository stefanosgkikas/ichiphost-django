from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h1> The Django Homepage</h1>")
    return render(request, 'pages/home.html')

def contact(request):
    #return HttpResponse("<h1> The Django Homepage</h1>")
    return render(request, 'pages/contact.html') 

def about(request):
    #return HttpResponse("<h1> The Django Homepage</h1>")
    return render(request, 'pages/about.html') 