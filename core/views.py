from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
