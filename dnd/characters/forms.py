from django.forms import ModelForm
from .models import Character

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = [
        'name',
        'level',
        'character_class',
        'background',
        'player_name',
        'race',
        'alignment',
        'experience_points',
    ]