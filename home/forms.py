from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label="User Name :")
    first_name = forms.CharField(max_length=100, label="First Name :")
    last_name = forms.CharField(max_length=100, label="Last Name :")
    email = forms.EmailField(max_length=200, label="Email :")
    phone = forms.CharField(max_length=200, label="Phone :")
    facebook = forms.CharField(max_length=100, label="Facebook :")
    skype = forms.CharField(max_length=100, label="Skype :")
    contact_detail = forms.CharField(max_length=100, label="Contact Detail :")
    biography = forms.CharField(widget=forms.Textarea)


    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2',)