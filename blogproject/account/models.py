from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # AbstractUser: User에서 동작은 그대로, 필드 추가
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    major = models.CharField(max_length=50)