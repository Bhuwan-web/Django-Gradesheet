from django.urls import path

from admission.api_view import AdmissionModelViewSet, TeachersInfoModelViewSet
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/admission", AdmissionModelViewSet, basename="api-admission")
router.register("api/teachers-info", TeachersInfoModelViewSet, basename="api-teachers-infp")


app_name = "admission"
urlpatterns = [
    path("admission", views.AdmissionFormView.as_view(), name="admission"),
    path("basic-info/", views.UserInfoFormView.as_view(), name="basic_info"),
]
urlpatterns += router.urls
