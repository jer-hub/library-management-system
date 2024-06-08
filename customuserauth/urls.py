from django.urls import path
from .views import CustomLoginView, CustomRegisterView, registration


app_name = "customuserauth"
urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", CustomRegisterView.as_view(), name="register"),
]