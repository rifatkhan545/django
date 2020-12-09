from django.shortcuts import render, redirect
from .forms import UserSignupForm
from django.contrib.auth.models import User


def profile(request):
    return render(request, 'profile.html')


def signup(request):
    if request.method == 'POST' :
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data_get('user')
            email = form.cleaned_data_get('email')
            password = form.cleaned_data_get('password')
            User.objects.create_user(username=user, email= email, password= password)
            return redirect('index')
    else:
        form = UserSignupForm()
    context ={'form' : form}
    return render(request, 'signup.html')


def login(request):
    return render(request,'login.html')



