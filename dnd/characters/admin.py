from django.contrib import admin
from .models import Character

# Register your models here.


class CharacterAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'name',
        'level', 
        'character_class',
        'player_name',
        'race',
        'alignment',
        'experience_points',
        'slug'
    ]
    prepopulated_fields = {'slug': ('name', 'player_name', 'character_class', 'race')}

admin.site.register(Character, CharacterAdmin)