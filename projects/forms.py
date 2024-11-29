# projects/forms.py
from django import forms
from .models import Project
from .models import ProjectApplication

class ProjectApplicationForm(forms.ModelForm):
    class Meta:
        model = ProjectApplication
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write a message to the project owner...',
                'class': 'form-control'
            }),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'skills_required', 'budget', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your project'}),
            'skills_required': forms.TextInput(attrs={'placeholder': 'e.g., photography, video editing'}),
            'budget': forms.NumberInput(attrs={'placeholder': 'Estimated budget'}),
            'location': forms.TextInput(attrs={'placeholder': 'Optional: City or Remote'}),
        }
