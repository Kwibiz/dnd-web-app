from django.urls import path
from . import views

app_name = 'characters'
urlpatterns = [
    path('create/', views.create_character, name='create_character'),
    path('list/<slug:slug>', views.detailed_character, name='detailed_character')
]