from django import forms
from .models import CourseModel


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = "__all__"

    def __str__(self):
        return self.cleaned_data["name"]
