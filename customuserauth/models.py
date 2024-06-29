from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
class CustomUserModel(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=64, blank=True, null=True, unique=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
