from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')


def contract(request):
    return render(request, 'core/contact.html')
