from django import forms
from .models import CourseModel


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = "__all__"
