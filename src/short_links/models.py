from django.db import models


class Link(models.Model):
    full_url = models.URLField()
    short_url = models.URLField(null=True, unique=True)
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_url
