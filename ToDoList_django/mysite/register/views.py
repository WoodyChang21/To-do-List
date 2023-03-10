from django.shortcuts import render, redirect
#This is the built in sign-in form
from .forms import RegisterForm

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("/home")
        
    else: 
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})