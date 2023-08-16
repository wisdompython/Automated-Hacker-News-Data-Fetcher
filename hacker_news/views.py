from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Items,Comments
from django.core.paginator import Paginator
import json

def paginator(request,model_items):
    paginator = Paginator(model_items, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj

def news(request):
    items =Items.objects.filter(type='story')
    page_obj = paginator(request,items)
    return render (request,'home.html',{'page_obj':page_obj,'no_pages':page_obj.paginator.page_range})
def comments(request,id):
    item = Items.objects.get(id=id)
    comment = Comments.objects.filter(item=item)
    return render(request, 'comments.html', {'comments':comment,'item':item, 'comment_count':comment.count()})

def jobs(request):
    jobs = Items.objects.filter(type='poll')
    page_obj = paginator(request,jobs)
    return render(request, 'jobs.html',{'page_obj':page_obj,'no_pages':page_obj.paginator.page_range})

def ShowHN(request):
    pass

def AskHN(request):
    pass

