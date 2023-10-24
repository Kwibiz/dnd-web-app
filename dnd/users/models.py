from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='First Name')
    last_name = models.CharField(max_length=20, verbose_name='Last Name')
    role = models.CharField(choices=[('DM', 'Dungeon Master'), ('Player', 'Player')], max_length=30, verbose_name='Role')