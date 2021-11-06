from django.urls import path

from home import api_views
from . import views
from UserAuth.views import LogoutView

app_name = "home"
urlpatterns = [
    path("home", views.home, name="home"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("api/home", api_views.HomeAPIView.as_view(), name="api-home"),
]
