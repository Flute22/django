from django.shortcuts import render
from .models import ChaiVerity
from django.shortcuts import get_object_or_404

# Create your views here.
def myapp_home(request): 
    chais = ChaiVerity.objects.all()
    return render(request, 'myapp/app.html', {'chais': chais})

def chai_detail(request, chai_id): 
    chai = get_object_or_404(ChaiVerity, pk = chai_id)
    return render(request, 'myapp/chai-detail.html', {'chai': chai})