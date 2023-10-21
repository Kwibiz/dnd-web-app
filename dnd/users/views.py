from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.contrib.auth.views import LoginView

# Create your views here.

@login_required
def users_main(request):
    user = request.user.username
    return render(request, 'users/users_main.html', context={'user': user})


def logout_view(request):
    logout(request)


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    next_page = 'users_main'
    redirect_authenticated_user = True