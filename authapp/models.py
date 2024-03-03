from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True) #добавить default
    nickname = models.CharField(verbose_name='никнэйм', max_length=64, blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=21)

class ShopUserProfile(models.Model):
    user = models.OneToOneField(
        ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE
    )
    tagline = models.CharField(verbose_name='интересы', max_length=256, blank=True)
    aboutMe = models.CharField(verbose_name='о себе', max_length=512, blank=True)
    city = models.CharField(verbose_name='город', max_length=64, blank=True)
    country = models.CharField(verbose_name='страна', max_length=64, blank=True)

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()



