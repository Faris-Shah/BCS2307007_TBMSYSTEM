from django.db import models

# Create your models here.
class Activity(models.Model):
   Activity_id = models.CharField(max_length=10)
   Name = models.TextField()
   Desc = models.TextField()
   Date = models.DateField()