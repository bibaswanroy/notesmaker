from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    username = models.CharField(max_length=50, default='')
