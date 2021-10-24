from django import forms
from django.forms import fields, models
from .models import Login
class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=('email','username','password')

class MyForm(forms.Form):
    name=forms.CharField(label="Name", max_length=120, required=False)

