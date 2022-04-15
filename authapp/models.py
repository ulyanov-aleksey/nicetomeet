from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField


#
from django.utils.timezone import now


class Contacts(AbstractUser):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )
    avatar = ResizedImageField(size=[200, 200], upload_to='users_avatar/', verbose_name='аватар', blank=True,
                               force_format='png')
    age = models.PositiveSmallIntegerField(verbose_name='возраст', default=18)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))
    country = models.CharField(max_length=50, verbose_name='страна', blank=True)
    sity = models.CharField(max_length=50, verbose_name='город', blank=True)
    district = models.CharField(max_length=50, verbose_name='район', blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    def __str__(self):
        return self.username

    # def is_activation_key_expire(self):
    #     if now() <= self.activation_key_expires:
    #         return False
    #     return True


# Create your models here.
