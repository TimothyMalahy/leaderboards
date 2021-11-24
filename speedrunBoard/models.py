from django.db import models
from django.db.models.fields import CharField
from core.models import Game, RomHack

# Create your models here.

class Categories(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Submission(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    romHack = models.ForeignKey(RomHack, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
    duration = models.DurationField()
