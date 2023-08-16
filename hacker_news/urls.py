from django import views
from django.contrib import admin
from django.urls import path
from .views import news, comments, jobs


urlpatterns=[
    path('',news, name='news'),
    path('comments/<id>', comments, name='comment'),
    path('jobs/', jobs, name='jobs')
]

