from django.urls import path, include
from blogs import views

urlpatterns = [
    path('home', views.home),
    path('about', views.about),
]
