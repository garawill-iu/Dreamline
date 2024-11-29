from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_project, name='create_project'),
    path('', views.marketplace, name='marketplace'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('<int:project_id>/apply/', views.apply_to_project, name='apply_to_project'),  # New URL for applying
]
