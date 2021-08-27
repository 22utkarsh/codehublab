from django.contrib import admin
from django.urls import path
from codehubapp import views

urlpatterns = [
   path("",views.index,name='index'),
   path("courses",views.courses,name='courses'),
   path("home",views.home,name='home'),
   path("contact",views.contact,name='contact'),
   path("blog",views.blog,name='blog')
]