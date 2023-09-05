from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from backend import views


urlpatterns = [
    
    path("", views.index, name="home"),
    path("index/", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact")
]
