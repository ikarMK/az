from django.db import models

class user(models.Model):
    ip = models.AutoField(unique=True,primary_key=True)
    count = models.IntegerField(primary_key=False)

# Create your models here.
