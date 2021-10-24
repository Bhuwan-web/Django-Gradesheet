from typing import Generic
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import TemplateView

from admission.forms import UserAdmissionForm, UserInfoForm
from admission.models import StudentInfo, UserAdmission

# Create your views here.
def admission_form_view(request):
    form=UserAdmissionForm()
    context={
        "header":"Admission Form",
        "title":"Admission Form",
        "form":form
    }
    return render(request,'admission/admission_form.html',context)

# def user_info_view(request):
#     form=UserInfoForm()
#     context={
#         "title":"User Basic Info",
#         "header":"User Basic Info",
#         "form":form
#     }
#     return render(request,'UserAuth/login.html',context)
class UserInfoFormView(FormView):
    form_class=UserInfoForm
    template_name='UserAuth/login.html'
    extra_context={
        "title":"User Basic Info",
        "header":"User Basic Info",
        "form":form_class
    }
    success_url="/"
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class StudentInfoFormView(FormView):
    form_class=StudentInfo
    template_name='UserAuth/login.html'
    extra_context={
        "title":"Student Basic Info",
        "header":"Student Basic Info",
        "form":form_class
    }