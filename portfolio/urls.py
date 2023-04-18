from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('workexperience/', views.workexperience, name='workexperience'),
    path('project/', views.project, name='project'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('contact/', views.contact, name='contact'),
]