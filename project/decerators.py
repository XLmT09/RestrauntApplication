from django.shortcuts import redirect
from django.urls import reverse

# A decerator which checks if the current user is in a particular group before accessing
# the page, if the user is not in a specified group they get sent to the login page.
def group_required(group_name):
    # param view_fun the function which the decerator will be applied to
    def decerator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated or not request.user.groups.filter(name=group_name).exists():
                # Redirect to the login URL
                return redirect(reverse("account-login"))
            response = view_func(request, *args, **kwargs)
            return response
        return wrapper
    return decerator