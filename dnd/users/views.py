from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

@login_required(login_url='login')
def users_main(request):
    user = request.user.username
    return render(request, 'users/users_main.html', context={'user': user})


class LogoutUserView(LogoutView):
    next_page = 'users_main'
    

class LoginUserView(LoginView):
    template_name = 'users/login.html'
    next_page = 'users_main'
    redirect_authenticated_user = True