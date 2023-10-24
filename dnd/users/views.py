from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from characters.models import Character


@login_required(login_url='users:login')
def profile(request):
    user_username = request.user.username
    user_id = request.user.id
    characters = Character.objects.filter(user_id=user_id)
    return render(request, 'users/profile.html', 
                  context={
                      'user': user_username, 
                      'characters': characters
                      })


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('users:users_main')
    
    else:
        form = UserCreationForm()

    return render(request, 'users/sign_up.html', context={'form': form,})


class LogoutUserView(LogoutView):
    next_page = 'users:users_main'
    

class LoginUserView(LoginView):
    template_name = 'users/login.html'
    next_page = 'users:users_main'
    redirect_authenticated_user = True