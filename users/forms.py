import users.models as models

from django.contrib.auth.forms import UserCreationForm


class RegisterUser(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
