from django.urls import path
from rest_framework import routers
from .views import CourseView
from rest_framework.routers import DefaultRouter
from .rest_view import CourseListView

router = DefaultRouter()
router.register("api/course", CourseListView, basename="api-course")

app_name = "course"
urlpatterns = [
    path("course", CourseView.as_view(), name="course"),
]
urlpatterns += router.urls
