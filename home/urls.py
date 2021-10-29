from django.urls import path
from . import views
from UserAuth.views import LogoutView
app_name="home"
urlpatterns = [
    path("home",views.home,name="home"),
    path("logout",LogoutView.as_view(),name="logout"),
]
