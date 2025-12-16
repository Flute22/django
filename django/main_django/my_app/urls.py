from django.urls import path
from . import views

urlpatterns = [
    path('', views.myapp_home, name='myapp_home'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
] 