from typing import Generic
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import TemplateView

from admission.forms import UserAdmissionForm, UserInfoForm
from admission.models import StudentInfo, UserAdmission, UserInfo

# Create your views here.


class AdmissionFormView(FormView):
    form_class = UserAdmissionForm
    template_name = "admission/admission_form.html"
    extra_context = {
        "header": "Admission Form",
        "title": "Admission Form",
        "form": form_class,
        # "formdict":form_class.__dict__,
    }


class UserInfoFormView(FormView):
    form_class = UserInfoForm
    template_name = "UserAuth/login.html"
    extra_context = {"title": "User Basic Info", "header": "User Basic Info", "form": form_class}
    success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class StudentInfoFormView(FormView):
    form_class = StudentInfo
    template_name = "UserAuth/login.html"
    extra_context = {"title": "Student Basic Info", "header": "Student Basic Info", "form": form_class}
