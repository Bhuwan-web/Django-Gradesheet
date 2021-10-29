from django import forms
from django.contrib.auth.forms import UsernameField
from django.utils.translation import gettext_lazy as _
from admission.models import StudentInfo, UserAdmission
from customUser.models import User
from customUser.admin import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
        field_classes = {"email": UsernameField}

    def clean_email(self):
        email = self.cleaned_data["email"]
        # print(bool(UserAdmission.objects.get(parents_info__email=email)))
        try:
            UserAdmission.objects.get(student_info__email=email)
            return email
        except:
            try:
                UserAdmission.objects.get(parents_info__email=email)
                return email
            except:
                raise forms.ValidationError("Only the admitted student's can create their accounts")


class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password")


class MyForm(forms.Form):
    name = forms.CharField(label="Name", max_length=120, required=False)
