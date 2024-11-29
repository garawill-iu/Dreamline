# projects/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProjectForm, ProjectApplicationForm
from .models import Project

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})


def marketplace(request):
    query = request.GET.get('q', '')  # Get the search query from the URL
    projects = Project.objects.all()
    if query:
        projects = projects.filter(title__icontains=query)  # Filter projects by the search query
    return render(request, 'projects/marketplace.html', {'projects': projects, 'query': query})


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            messages.success(request, "Project created successfully!")
            return redirect('marketplace')  # Adjust the redirect as needed
    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})


@login_required
def apply_to_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.project = project
            application.user = request.user
            application.save()
            messages.success(request, "You have successfully applied to the project.")
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectApplicationForm()
    return render(request, 'projects/apply_to_project.html', {'form': form, 'project': project})
