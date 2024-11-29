from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, EditProfileForm
from django.db.models import Q  # Import Q for complex lookups
from .models import CustomUser

def search_users(request):
    query = request.GET.get('q')  # Get search query from URL
    results = []
    if query:
        results = CustomUser.objects.filter(
            Q(username__icontains=query) |  # Search by username
            Q(skills__icontains=query) |   # Search by skills
            Q(location__icontains=query)   # Search by location
        )
    return render(request, 'users/search_results.html', {'results': results, 'query': query})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def homepage(request):
    return render(request, 'users/homepage.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')  # Redirect to the profile page
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'users/edit_profile.html', {'form': form})
