from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('signup/', views.sign_up, name='sign_up'),
    path('main/', views.users_main, name='users_main'),
]