from django.conf import settings
from django.db import models

class Family(models.Model):
    name= models.CharField(max_length=40)
    age= models.IntegerField()
    creation_date=models.DateField(blank=True, null=True)
