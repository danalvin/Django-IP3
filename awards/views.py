from django.shortcuts import render, redirect
from .models import *
from .forms import ProjectForm
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
    projecth = Project.objects.get(id=project_id)
    return render(request, 'projects.html', {'project': projecth})


def search_results(request):
    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_articles = Project.search_project(search_term)
        message = "{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def new_project(request):
    current_user = request.user
    profiles = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.profile = profiles
            project.save()
        return redirect('index')
    else:
        form = ProjectForm()
    return render(request, 'upload.html', {"form": form})
