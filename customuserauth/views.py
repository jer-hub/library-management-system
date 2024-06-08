from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .models import CustomUserModel
from .forms import RegisterForm, CustomAuthenticationForm


# Create your views here.
class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "auth/login.html"

    def get_success_url(self):
        return reverse_lazy("home")


class CustomRegisterView(CreateView):
    model = CustomUserModel
    form_class = RegisterForm
    template_name = "auth/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


def registration(request):
    if request.method == "POST":
        # Create a form that has request.POST
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("customuserauth:login")  # Redirect to the login page
        else:
            # Handle password mismatch error here
            form.add_error("password2", "Passwords entered do not match")
    else:
        form = RegisterForm()
    return render(request, "auth/register.html", {"form": form})
