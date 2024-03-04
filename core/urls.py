from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name='index'),
    path('<str:slug>',content_details, name='content'),
    path('search/',search, name='search'),
    path('category/',category, name='category'),
]