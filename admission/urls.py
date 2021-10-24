from django.urls import path
from . import views
urlpatterns = [
    path("admission",views.admission_form_view,name="admission"),
    path("basic-info/",views.UserInfoFormView.as_view(),name="basic_info")
]
