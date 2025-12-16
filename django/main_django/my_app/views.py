from django.shortcuts import render

# Create your views here.
def myapp_home(request): 
    return render(request, 'myapp/app.html')