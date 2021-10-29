from django.contrib import admin
from django.db import models
from .models import User
from django.contrib.auth.admin import UserAdmin
from django import forms

# Register your models here.


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "username", "role")

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_filter = ("is_active", "role")
    search_fields = ("username", "email", "roles")
    ordering = ("-last_login",)
    list_display = ("email", "username", "first_name", "role")
    fieldsets = (
        (None, {"fields": ("username", "email", "role")}),
        ("Personal Details", {"fields": ("first_name", "last_name", "date_of_birth")}),
        ("Permissions", {"fields": ("is_active", "is_admin")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "role", "password1", "password2"),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
