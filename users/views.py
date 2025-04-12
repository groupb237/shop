from django.shortcuts import render, redirect

import users.forms as forms


# Create your views here.

def register_user(request):
    if request.POST:
        form = forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    form = forms.RegisterUser()
    return render(request, "auth/form.html",
                  context={"form": form})
