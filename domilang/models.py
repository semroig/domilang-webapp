from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    native_lan = models.CharField(max_length=24, default='none')
    foto = models.ImageField(null=True, blank=True, default='generic_profile_pic.png')
    pais = models.CharField(max_length=24, default='none')
    franja = models.CharField(max_length=24, default='none')
    nivel = models.CharField(max_length=24, default='none')
    study_lan = models.CharField(max_length=24, default='none')
    phone = models.CharField(max_length=24, default='none')
    role = models.CharField(max_length=12, default='none')

class StudyModule(models.Model):
    title = models.CharField(max_length=36, default='none')
    description = models.CharField(max_length=255, default='none')
    assigned_to = models.ManyToManyField(User, related_name='homework', blank=True)

    def __str__(self):
        return self.title