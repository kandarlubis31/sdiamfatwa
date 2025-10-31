from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from functools import wraps

def staff_required(view_func):
    """
    Decorator for views that checks that the user is a staff member,
    redirecting to the log-in page if necessary.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_active and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        return redirect_to_login(request.get_full_path())
    return _wrapped_view

def redirect_to_login(next, login_url=None, redirect_field_name='next'):
    from django.contrib.auth.views import redirect_to_login as auth_redirect_to_login
    return auth_redirect_to_login(next, login_url, redirect_field_name)

class JazzminLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Check if the user is trying to access the admin panel
        if request.path.startswith('/admin_panel/'):
            if not request.user.is_authenticated or not request.user.is_staff:
                from django.contrib.auth.views import redirect_to_login
                return redirect_to_login(request.get_full_path())
        return None