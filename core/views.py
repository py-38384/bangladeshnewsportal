from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import Http404
from django.conf import settings
from django.core.paginator import Paginator
from .models import *

def index(request):
    context = {}
    highlighted_content = []
    page_number = request.GET.get('page')
    if page_number:
        page_number = int(page_number)
    else:
        page_number = 1
    all_content = Content.objects.all()
    for content in all_content:
        if content.highlighted and len(highlighted_content)<5:
            highlighted_content.append(content)
    p = Paginator(all_content,settings.DEFAULT_PRODUCT_LIMIT_PER_PAGE)
    content_obj = p.get_page(page_number)
    context['content_obj'] = content_obj
    if len(highlighted_content)==5:
        context['highlighted_content'] = highlighted_content
    return render(request,'core/index.html',context)

def content_details(request,slug):
    context = {}
    if Content.objects.filter(slug=slug).exists():
        content_obj = Content.objects.get(slug=slug)
        content_obj.views += 1
        content_obj.save()
        related_content_obj = Content.objects.filter(category=content_obj.category).exclude(slug=slug)[0:3]
        context['content'] = content_obj
        context['related_content'] = related_content_obj
        return render(request,'core/content_details.html',context)
    raise Http404()

def search(request):
    context = {}
    q = request.GET.get('q')
    page_number = request.GET.get('page')
    if page_number:
        page_number = int(page_number)
    else:
        page_number = 1
    if q:
        all_content = Content.objects.filter(Q(title__icontains=q)|Q(content__icontains=q)|Q(author__full_name__icontains=q)|Q(brief__icontains=q)|Q(category__name__icontains=q))
        p = Paginator(all_content,settings.DEFAULT_PRODUCT_LIMIT_PER_PAGE)
        content_obj = p.get_page(page_number)
        context['content_obj'] = content_obj
        context['q'] = q
        if content_obj.has_next():
            context['next'] = page_number+1
        if content_obj.has_previous():
            context['previous'] = page_number-1
        return render(request,'core/search.html',context)
    return redirect('index')

def category(request):
    context = {}
    category = request.GET.get('category')
    page_number = request.GET.get('page')
    if page_number:
        page_number = int(page_number)
    else:
        page_number = 1
    if category:
        category_obj = Category.objects.get(name=category)
        all_content = Content.objects.filter(category=category_obj)
        p = Paginator(all_content,settings.DEFAULT_PRODUCT_LIMIT_PER_PAGE)
        content_obj = p.get_page(page_number)
        context['content_obj'] = content_obj
        context['current_category'] = category
        if content_obj.has_next():
            context['next'] = page_number+1
        if content_obj.has_previous():
            context['previous'] = page_number-1
        return render(request,'core/category.html',context)
    raise Http404()
    