from django.http import HttpResponse
from django.shortcuts import render

def home(request): 
    # return HttpResponse("Hello World! You are at Django Home page.")
    return render(request, 'website/index.html')    

def about(request): 
    return HttpResponse("Hello World! You are at Django About page.")

def contact(request): 
    return HttpResponse("Hello World! You are at Django Contact page.")
