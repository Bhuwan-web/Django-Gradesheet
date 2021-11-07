from django.http.response import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from UserAuth.forms import LoginForm
from customUser.models import User
from admission.models import ParentsInfo, UserAdmission
from admission.teachers_model import TeachersInfoModel
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = "UserAuth/login.html"
    redirect_authenticated_user = True
    extra_context = {"title": "Login Form", "header": "Login", "form": LoginForm}

    def form_valid(self, form):
        return super().form_valid(form)


class SignupView(CreateView):
    template_name = "UserAuth/login.html"
    form_class = CustomUserCreationForm
    success_url = "/login"

    def is_teacher(self, query, email):
        try:
            admissionInfo = query.objects.get(email=email)
            return {"query": admissionInfo, "value": True}
        except:
            return {"query": "", "value": False}

    def is_student(self, query, email):
        try:
            admissionInfo = query.objects.get(student_info__email=email)
            return {"query": admissionInfo, "value": True}
        except:
            return {"query": "", "value": False}

    def is_parents(self, query, email):
        try:
            admissionInfo = query.objects.get(email=email)
            return {"query": admissionInfo, "value": True}
        except:
            return {"query": "", "value": False}

    def form_valid(self, form):
        """If the form is valid, save the associated model."""

        email = form.cleaned_data["email"]
        self.object = form.save()
        user = User.objects.get(email=email)

        is_student = self.is_student(UserAdmission, email)
        is_parents = self.is_parents(ParentsInfo, email)
        print(is_parents)
        is_teacher = self.is_teacher(TeachersInfoModel, email)

        if is_parents["value"]:
            admissionInfo = is_parents["query"]
            user.role = "Parents"
            user.first_name = admissionInfo.f_name
            user.last_name = admissionInfo.l_name
            user.save()
        elif is_student["value"]:
            admissionInfo = is_student["query"]
            user.first_name = admissionInfo.basic_info.f_name
            user.last_name = admissionInfo.basic_info.l_name
            user.date_of_birth = admissionInfo.basic_info.date_of_birth
            user.save()
        elif is_teacher["value"]:
            admissionInfo = is_teacher["query"]
            user.role = "Teacher"
            user.first_name = admissionInfo.f_name
            user.last_name = admissionInfo.l_name
            user.username = admissionInfo.short_name
            user.save()

        return HttpResponseRedirect(self.get_success_url())


class CustomLogoutView(LogoutView):
    template_name = "UserAuth:login"
