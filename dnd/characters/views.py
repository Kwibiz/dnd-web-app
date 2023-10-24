from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Character


class CreateCharacterView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = Character
    template_name = 'characters/create_character.html'
    fields = '__all__'
    success_url = reverse_lazy('characters:create_character')