from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Profile, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ("email",)
    list_display = ("email", "is_active", "is_staff", "date_joined")
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_active", "is_staff"),
        }),
    )
    filter_horizontal = ("groups", "user_permissions")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "created_at")
    search_fields = ("user__email", "first_name", "last_name")