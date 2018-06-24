from django.core.exceptions import PermissionDenied

def superuser_only(function):

    def func(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied           
        return function(request, *args, **kwargs)
    return func