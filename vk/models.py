from django.db import models
from datetime import datetime


class Account(models.Model):
    link = models.CharField(max_length=60, unique=True, null=False, blank=False)
    added = models.BooleanField(default=False)
    date_added = models.DateField(auto_now=True, default=datetime.now())