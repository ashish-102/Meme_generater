from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class User_signup(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(), label='Password', required=True)
    password2 = forms.CharField(
        widget=forms.PasswordInput(), label='Password (Confirm)', required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

        labels = {
            'username': 'Username',
            'email': 'Email-id',
        }
        
        widgets = {
            'email': forms.EmailInput()
        }


class User_login(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
    ), label='Username', required=True, label_suffix='')
    password = forms.CharField(widget=forms.PasswordInput(
    ), label='Password', required=True, label_suffix='')
