from django.urls import path
from . import views

app_name = 'characters'
urlpatterns = [
    path('create/', views.create_character, name='create_character'),
]