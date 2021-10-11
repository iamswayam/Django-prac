from django.contrib import admin
from django.urls import path, include
from .views import TestView, HomePage

urlpatterns = [
    path('', HomePage, name='HomePage'),
    path('test/', TestView.as_view(), name='TestView'),
]
