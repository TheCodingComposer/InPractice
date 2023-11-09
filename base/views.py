from django.shortcuts import render, redirect

def home(request):
    return render(request, 'main/home.html')

def login(request):
    return render(request, 'base/login.html')

def register(request):
    return render(request, 'base/register.html')
