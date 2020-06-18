from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, FileInput, EmailInput

from home.models import UserProfile


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
        }



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone','biography', 'facebook','skype','contact_detail', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'skype': TextInput(attrs={'class': 'input', 'placeholder': 'skype'}),
            'biography': TextInput(attrs={'class': 'input', 'placeholder': 'biography'}),
            'facebook': TextInput(attrs={'class': 'input', 'placeholder': 'facebook'}),
            'contact_detail': TextInput(attrs={'class': 'input', 'placeholder': 'contact_detail'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }