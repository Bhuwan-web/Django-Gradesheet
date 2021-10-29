from django.urls import path
from . import views


app_name="UserAuth"
urlpatterns = [
    path("login/",views.CustomLoginView.as_view(),name="login"),
    path("",views.CustomLoginView.as_view()),
    path("signup/",views.SignupView.as_view(),name="signup"),

    # path("",views.trial,name="trial")
]
