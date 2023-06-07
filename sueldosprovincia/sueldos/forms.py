from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={'class': 'form-control inputs', 'placeholder':'DNI', 'autofocus':'autofocus', 'maxlengh':'8'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control inputs', 'placeholder':'Contraseña'})
    )
