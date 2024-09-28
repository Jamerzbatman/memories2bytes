from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home_view(request):
    return render(request, 'pages/homepage.html')

def about_view(request):
    return render(request, 'pages/aboutpage.html')

def pricing_view(request):
    return render(request, 'pages/pricingpage.html')

def process_view(request):
    return render(request, 'pages/processpage.html')

def logout_view(request):
    logout(request)
    return redirect('/')
