from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import index, tags, categories, PostDetails, Contact, Contactsuccess

urlpatterns = [
    path('', index, name = 'index'),
    path('categories/<slug:category_slug>', categories, name ='category'),
    path('tags/<slug:tag_slug>', tags, name ='tag'),
    path('<slug:post_slug>', PostDetails, name ='post_details'),
    path('contact/', Contact, name = 'contact'),
    path('contact/contactsuccess/', Contactsuccess, name ='contactsuccess')

]