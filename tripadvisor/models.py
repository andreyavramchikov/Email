from django.db import models


class Restaurant(models.Model):
    email = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    postal = models.CharField(max_length=255, blank=True)
    hash = models.CharField(max_length=255, null=False, unique=True)
    sent = models.BooleanField(default=False)