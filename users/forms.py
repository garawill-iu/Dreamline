from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['bio', 'location', 'skills', 'portfolio_url']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself...'}),
            'location': forms.TextInput(attrs={'placeholder': 'Your location'}),
            'skills': forms.TextInput(attrs={'placeholder': 'Your skills (e.g., photography, editing)'}),
            'portfolio_url': forms.URLInput(attrs={'placeholder': 'Link to your portfolio'}),
        }
