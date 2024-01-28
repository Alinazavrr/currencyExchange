# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import PaidUser

def create_or_update_extended_user(sender, instance, created, **kwargs):
    if created:
        PaidUser.objects.create(user=instance)
    else:
        instance.extendeduser.save()