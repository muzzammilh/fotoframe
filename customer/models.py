from django.db import models
from django.contrib.auth.models import AbstractUser

from misc.models import BaseModel

class AppUser(AbstractUser, BaseModel):
    username = None
    email = models.EmailField('email address', unique=True)
    profile_pic = models.ImageField(upload_to ='uploads/% Y/% m/% d/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []