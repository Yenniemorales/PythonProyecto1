from django.db import models

# Create your models here.

class Centro(models.Model):
    lugar = models.CharField(max_length=30)
    numero= models.IntegerField()