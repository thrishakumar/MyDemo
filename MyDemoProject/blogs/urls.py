from django.urls import path, include
from blogs import views

urlpatterns = [
    path('', views.home ,name='home-url'),
    path('about', views.about,name='about-url'),
    path('createpost', views.createPost,name='createpost-url'),
]
