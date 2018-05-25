from django.urls import path

from . import views

urlpatterns = [
    path('add_student/', views.add_student, name='add_student'),
    path('add_school/', views.add_school, name='add_school'),
    path('attendance/', views.attendance, name='attendance'),
    path('', views.home, name='home'),
    
]