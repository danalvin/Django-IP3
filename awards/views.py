from django.shortcuts import render, redirect

# Create your views here.
def loader(request):
    return render(request, 'loader.html')


def index(request):
    return render(request, 'index.html')