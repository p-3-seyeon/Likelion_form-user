from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(upload_to='image/', default='')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)