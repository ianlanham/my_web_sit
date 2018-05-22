from django.urls import path

from . import views

urlpatterns = [
    path('add_student/', views.add_student, name='add_student'),
    path('', views.home, name='home'),
    
]