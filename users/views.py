from django.shortcuts import render

import users.forms as forms


# Create your views here.

def register_user(request):
    form = forms.RegisterUser()
    return render(request, "auth/form.html",
                  context={"form": form})
