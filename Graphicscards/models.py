from django.db import models
from django.contrib.auth.models import User

class GraphicsCards(models.Model):
    id_graphics_cards = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    price = models.FloatField(max_length=255)
    graphics_chip = models.CharField(max_length=45)


class Post(models.Model):
    post = models.CharField(max_length=500)




