from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=50, verbose_name='Character Name')
    level = models.IntegerField(default=1, verbose_name='Level')
    experience_points = models.IntegerField(default=0, verbose_name='Experience Points')
    character_class = models.CharField(max_length=20, verbose_name='Class')
    background = models.TextField(blank=True, null=True, verbose_name='Background')
    race = models.CharField(choices=[('Dragonborn', 'Dragonborn'), ('Dwarf', 'Dwarf'), ('Elf', 'Elf'), ('Gnome', 'Gnome'), ('Half Elf', 'Half Elf'), ('Half Orc', 'Half Orc'), ('Halfling', 'Halfling'), ('Human', 'Human'), ('Tiefling', 'Tiefling')], max_length=30, verbose_name='Race')
    alignment = models.CharField(max_length=70, verbose_name='Alignment')
    player_name = models.CharField(max_length=50, verbose_name="Player's name")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name' , 'player_name', 'character_class', 'race'], name='name of constraint')
        ]