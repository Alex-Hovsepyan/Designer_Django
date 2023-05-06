from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('explore/', views.explore, name='explore'),
    path('trending/', views.trending, name='trending'),
    path('contact/', views.contact, name='contact'),
]