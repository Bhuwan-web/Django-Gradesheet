import django
from django.shortcuts import render

# from django.views.generic.edit import UpdateView
from .forms import CourseModelForm
from django.views.generic import CreateView, UpdateView

# Create your views here.


class CourseView(CreateView):
    template_name = "course/course.html"
    success_url = "course"
    form_class = CourseModelForm
