from django.http.response import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from UserAuth.forms import LoginForm
from customUser.models import User
from admission.models import StudentInfo, TeachersInfoModel, UserAdmission
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

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        email = form.cleaned_data["email"]
        self.object = form.save()
        user = User.objects.get(email=email)
        try:
            admissionInfo = UserAdmission.objects.get(student_info__email=email)
            user.first_name = admissionInfo.basic_info.f_name
            user.last_name = admissionInfo.basic_info.l_name
            user.date_of_birth = admissionInfo.basic_info.date_of_birth
            user.save()
        except:
            try:
                admissionInfo = TeachersInfoModel.objects.get(email=email)
                user.role = "Teacher"
                user.first_name = admissionInfo.f_name
                user.last_name = admissionInfo.l_name
                user.username = admissionInfo.short_name
                user.save()
            except:
                admissionInfo = UserAdmission.objects.filter(parents_info__email=email)
                user.role = "Parents"
                user.first_name = admissionInfo[0].parents_info.f_name
                user.first_name = admissionInfo[0].parents_info.f_name
                user.save()
        finally:
            return HttpResponseRedirect(self.get_success_url())


class CustomLogoutView(LogoutView):
    template_name = "UserAuth:login"
