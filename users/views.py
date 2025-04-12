from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

import users.forms as forms


# Create your views here.

def register_user(request):
    if request.POST:
        form = forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/auth/login")
        else:
            messages.error(request, message=f"{form.errors}")
    form = forms.RegisterUser()
    return render(request, "auth/form.html",
                  context={"form": form})


def login_user(request):
    if request.POST:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
    form = AuthenticationForm()
    return render(request, template_name="auth/form.html", context={"form": form})
