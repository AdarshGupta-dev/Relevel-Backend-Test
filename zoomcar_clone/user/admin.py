from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserModelAdmin(BaseUserAdmin):
    list_display = ("id", "email", "name", "gender",
                    "date_of_birth", "is_admin")
    list_filter = ("is_admin",)
    fieldsets = (
        ("User Credentials", {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("name", "gender", "date_of_birth",)}),
        ("Permissions", {"fields": ("is_admin",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "name", "date_of_birth", "password", "gender")
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserModelAdmin)
