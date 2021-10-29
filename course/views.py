import django
from django.shortcuts import render
from .forms import CourseModelForm
from django.views.generic import CreateView

# Create your views here.


class CourseView(CreateView):
    template_name = "course/course.html"
    success_url = "course"
    form_class = CourseModelForm
