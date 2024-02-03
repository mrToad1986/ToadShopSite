from django.db import models
from django.contrib.auth.models import AbstractUser

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True) #добавить default
    age = models.PositiveIntegerField(verbose_name='возраст', default=21)

class ShopUserProfile(models.Model):
    user = models.OneToOneField(
        ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE()
    )
    tagline = models.CharField(verbose_name='интересы', max_length=256, blank=True)
    aboutMe = models.CharField(verbose_name='о себе', max_length=512, blank=True)
    city = models.CharField(verbose_name='город', max_length=64, blank=True)
    country = models.CharField(verbose_name='страна', max_length=64, blank=True)
    #добавить дату регистрации