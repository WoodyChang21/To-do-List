from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        #The form will be baed on the "User" model, which means that the form will have fields for all the attributes of the "User"  model
        model= User
        #Specify which fields of the "User" model should be included in the form
        fields=["username", "email", "password1", "password2"]