from django.db import models


class Character(models.Model):
    RACE_CHOICES = (
        ("Dragonborn", "Dragonborn"),
        ("Dwarf", "Dwarf"),
        ("Elf", "Elf"),
        ("Gnome", "Gnome"),
        ("Half Elf", "Half Elf"),
        ("Half Orc", "Half Orc"),
        ("Halfling", "Halfling"),
        ("Human", "Human"),
        ("Tiefling", "Tiefling")
    )

    name = models.CharField(max_length=50, verbose_name='Character Name')
    level = models.PositiveIntegerField(default=1, verbose_name='Level')
    character_class = models.CharField(max_length=50, verbose_name='Class')
    background = models.TextField(verbose_name='Background', null=True, blank=True)
    player_name = models.CharField(max_length=50, verbose_name='Players Name')
    race = models.CharField(choices=RACE_CHOICES, max_length=20, verbose_name='Race')
    alignment = models.CharField(max_length=50, verbose_name='Alignment')
    experience_points = models.PositiveIntegerField(default=0, verbose_name='Experience Points')

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name' , 'player_name', 'character_class', 'race'], name='name of constraint')
        ]