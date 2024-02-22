from django.core.management.base import BaseCommand
from authapp.models import ShopUser, ShopUserProfile


class Command(BaseCommand):
    help = 'Update DB'

    def handle(self, *args, **kwargs):
        users = ShopUser.objects.all()
        for user in users:
            users_profile = ShopUserProfile.objects.create(user=user)
            users_profile.save()