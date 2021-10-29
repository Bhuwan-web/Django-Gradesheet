from django.urls import path
from . import views

app_name="admission"
urlpatterns = [
    path("admission",views.AdmissionFormView.as_view(),name="admission"),
    path("basic-info/",views.UserInfoFormView.as_view(),name="basic_info")
]
