
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_practitioner = models.BooleanField(default=False)


class Profile(models.Model):
    user = models\
        .ForeignKey(settings.AUTH_USER_MODEL,
                    on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username
