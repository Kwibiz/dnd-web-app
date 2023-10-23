from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Character

class CreateCharacterView(CreateView):
    model = Character
    template_name = 'characters/create_character.html'
    fields = '__all__'
    success_url = reverse_lazy('characters:create_character')