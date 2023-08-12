from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from misc.models import BaseModel

class AppUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('Email is required'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class AppUser(AbstractUser, BaseModel):
    username = None
    email = models.EmailField('email address', unique=True)
    profile_pic = models.ImageField(upload_to ='media/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()


class Post(BaseModel):
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='media/')
    description = models.TextField(blank=True, null=True)
    original_post = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    repost_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Post by {self.user_id.email}, ID: {self.id}"
