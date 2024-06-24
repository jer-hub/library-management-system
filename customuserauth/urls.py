from django.urls import path
from .views import CustomLoginView, CustomRegisterView, Logout


app_name = "customuserauth"
urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("logout/", Logout.as_view(), name="logout"),
]