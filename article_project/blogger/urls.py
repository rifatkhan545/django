from django.contrib import admin
from django.urls import path
from.views import login, signup, profile


urlpatterns = [
    path('', profile, name = 'profile'),
    path('login', login, name = 'login'),
    path('signup', signup, name = 'signup'),
]