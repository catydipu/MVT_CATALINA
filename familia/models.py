from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=100)
    age = models.FloatField()
    license = models.BooleanField()
