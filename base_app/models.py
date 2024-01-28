from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PaidUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    have_subscription = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username