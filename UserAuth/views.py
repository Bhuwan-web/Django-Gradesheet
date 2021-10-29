from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from UserAuth.forms import LoginForm, MyForm
from customUser.models import User
from admission.models import StudentInfo, UserAdmission
from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = "UserAuth/login.html"
    redirect_authenticated_user = True
    extra_context = {"title": "Login Form", "header": "Login", "form": LoginForm}

    def form_valid(self, form):
        return super().form_valid(form)


class SignupView(CreateView):
    template_name = "UserAuth/login.html"
    form_class = CustomUserCreationForm
    success_url = "login"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        email = form.cleaned_data["email"]
        self.object = form.save()
        try:
            admissionInfo = UserAdmission.objects.get(student_info__email=email)
            self.object.first_name = admissionInfo.basic_info.f_name
            self.object.first_name = admissionInfo.basic_info.f_name
            self.object.date_of_birth = admissionInfo.basic_info.date_of_birth
            self.object.save()
            return super().form_valid(form)
        except:
            admissionInfo = UserAdmission.objects.filter(parents_info__email=email)
            self.object.role = "Parents"
            self.object.first_name = admissionInfo[0].parents_info.f_name
            self.object.first_name = admissionInfo[0].parents_info.f_name
            self.object.save()
            return super().form_valid(form)


class CustomLogoutView(LogoutView):
    template_name = "UserAuth:login"
