from django.contrib import admin
from django.urls import path, include
from users import views  # Import the homepage view from the users app
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include users app URLs
    path('', views.homepage, name='homepage'),  # Add the homepage URL pattern
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Add login path
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Redirect to homepage
    path('search/', views.search_users, name='search_users'),  # Add this
    path('projects/', include('projects.urls')),  # Add this line
]

