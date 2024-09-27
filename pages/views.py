from django.shortcuts import render


def home_view(request):
    return render(request, 'pages/homepage.html')

def about_view(request):
    return render(request, 'pages/aboutpage.html')

def pricing_view(request):
    return render(request, 'pages/pricingpage.html')

def process_view(request):
    return render(request, 'pages/processpage.html')
