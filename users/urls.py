from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage
    path('register/', views.register, name='register'),  # Register page
    path('profile/', views.profile, name='profile'),  # Profile page
    path('edit-profile/', views.edit_profile, name='edit_profile'),  # Edit profile page
]
