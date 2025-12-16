from django.urls import path
from . import views

urlpatterns = [
    path('', views.myapp_home, name='myapp_home'),
] 