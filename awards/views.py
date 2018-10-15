from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def loader(request):
    return render(request, 'loader.html')


@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.get_all()
    return render(request, 'index.html', {'projects': projects})


def post(request):
    projects = Project.get_all()
    return render(request, 'page.html', {'projects': projects})


def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {'user': user})


def project(request, project_id):
    projecth = Project.objects.get(id = project_id)
    return render(request, 'projects.html', {'project': projecth})
