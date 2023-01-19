from django.db import models
from datetime import datetime
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    


# Create your models here.
