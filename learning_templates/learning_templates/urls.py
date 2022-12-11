"""learning_templates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from basic_app import views

urlpatterns = [
    path('', views.index, name='index'),  #it means go to views, grab the index and show it to the user on the home page
    path('admin/', admin.site.urls),
    path('basic_app/', include('basic_app.urls')), #cand cineva merge pe pagina noastra la basic_app/numele_unei_pagini, includem fisierul urls din basic_app si luam de acolo url urile
]
