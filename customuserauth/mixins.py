from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin

class RedirectUnauthenticatedUsersMixin:
    redirect_url = "home"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)
    

class RedirectNonStaffUsersMixin:
    redirect_url = "home"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.redirect_url)
        if not request.user.is_staff:
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)

class Is_AdministratorMixin(UserPassesTestMixin):
    def test_func(self):
        # Check if the user belongs to the "Administrators" group
        return self.request.user.groups.filter(name="Administrators").exists()

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        # You can redirect to a login page, display an access denied message, etc.
        return redirect('home') 
