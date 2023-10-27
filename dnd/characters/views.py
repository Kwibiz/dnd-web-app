from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify

from .models import Character
from .forms import CharacterForm



@login_required(login_url='users:login')
def create_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            user = request.user.id
            obj = form.save(commit=False)
            obj.user_id = user
            obj.slug = slugify(f'{form.cleaned_data["name"]} {form.cleaned_data["player_name"]} {form.cleaned_data["character_class"]} {form.cleaned_data["race"]}')
            obj.save()
            return redirect('characters:create_character')
    
    else:
        form = CharacterForm()

    return render(request, 'characters/create_character.html', context={'form': form})

@login_required(login_url='users:login')
def detailed_character(request, slug):
    character = Character.objects.get(slug=slug)
    return render(request, 'characters/detailed_character.html', context={'character':character})

# class CreateCharacterView(LoginRequiredMixin, CreateView):
#     login_url = reverse_lazy('users:login')
#     model = Character
#     template_name = 'characters/create_character.html'
#     fields = [
#         'name',
#         'level',
#         'character_class',
#         'background',
#         'player_name',
#         'race',
#         'alignment',
#         'experience_points',
#     ]
#     success_url = reverse_lazy('characters:create_character')