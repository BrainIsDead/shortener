from django.db import models

from accounts.models import User


class Link(models.Model):
    full_url = models.URLField(unique=True)
    short_url = models.URLField(null=True, unique=True)
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        related_name='links',
        on_delete=models.CASCADE
    )   

    def __str__(self):
        return self.full_url
