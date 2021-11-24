from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related

# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=150)

class Achievement(models.Model):
    difficulty_choices = [
        ('EASY','EASY'),
        ('MODERATE','MODERATE'),
        ('HARD','HARD'),
        ('INSANE','INSANE'),
    ]
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=40)

class UserAbstracted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievements = models.ManyToManyField(Achievement)


class Game(models.Model):
    name = models.CharField(max_length=150)
    platform = models.ManyToManyField(Platform)
    admins = models.ManyToManyField(User, related_name='game_admins')
    creator = models.ForeignKey(User, null=True, help_text='This is the user that created the game in the database, not the creator of the game.', on_delete=models.SET_NULL, related_name='game_creator')

class RomHack(models.Model):
    game = models.ForeignKey(Game, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='rom_hack_creator')
    link = models.URLField(max_length=300)
    description = models.TextField()
    achievements = models.ForeignKey(Achievement, null=True, on_delete=models.PROTECT)
    admins = models.ManyToManyField(User, related_name='rom_hack_admin')

