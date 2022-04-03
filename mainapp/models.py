from django.db import models
from django.contrib.auth.models import AbstractUser


#
class Contact(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', verbose_name='аватар', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='возраст', default=18)


# Create your models here.
