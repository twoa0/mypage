from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'introduction/index.html')

def intro(request):
    return render(request, 'introduction/index2.html')