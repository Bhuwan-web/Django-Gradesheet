from django import forms
from django.forms import fields, models

from admission.models import ParentsInfo, StudentInfo, UserAdmission, UserInfo


class UserAdmissionForm(forms.ModelForm):
    class Meta:
        model = UserAdmission
        fields = ("basic_info", "student_info", "parents_info")


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = "__all__"


class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = "__all__"


class ParentsInfoForm(forms.ModelForm):
    class Meta:
        model = ParentsInfo
        fields = "__all__"
