from django.urls import path
from .views import CourseView

app_name = "course"
urlpatterns = [
    path("course", CourseView.as_view(), name="course"),
]
