from django.shortcuts import redirect

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