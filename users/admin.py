from django.contrib import admin

import users.models as models


# Register your models here.


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ["password"]
    filter_horizontal = ["groups", "user_permissions"]
