from urllib import request
from django.apps import AppConfig
from django.shortcuts import render

class HackerNewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hacker_news'
    
    
    # def ready(self):
    #     from .import update_job
    #     update_job.start()
 