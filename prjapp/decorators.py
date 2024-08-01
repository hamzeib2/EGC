from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
from django.http import HttpResponseForbidden
from functools import wraps

def unauth_user(view_func):
    def wrapper_func(request , *args ,**kwargs):
        if request.user.is_authenticated:
            return redirect('store')
        else:
            return view_func(request , *args ,**kwargs)
    return wrapper_func

def auth_user(view_func):
    def wrapper_func(request , *args ,**kwargs):
        if request.user.is_anonymous:
            return redirect('login')
        else:
            return view_func(request , *args ,**kwargs)
    return wrapper_func


def is_admin(request):
    bool =False
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
        if group == 'admins':
            bool = True
    return bool

def admins(view_func):
    def wrapper_func(request , *args ,**kwargs):
        if is_admin(request):
            pass
        else:
            return redirect('store')
    return wrapper_func




def time_restrict(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        boo = is_admin(request)
        current_time = datetime.datetime.now().time()
        if current_time < datetime.time(9, 0, 0) or current_time > datetime.time(17, 0, 0):
            if boo == False:
                return HttpResponseForbidden("App is not available during this time")
        return view_func(request, *args, **kwargs)
    return wrapper

def allowed_users(allowed_roles= []):
    def decorator(view_func): 
        def wrapper_func(request , *args ,**kwargs):
            groub = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                print(group)
            if group in allowed_roles:
                return view_func(request , *args ,**kwargs)
            else:
                return redirect('store')
        return wrapper_func
    return decorator
