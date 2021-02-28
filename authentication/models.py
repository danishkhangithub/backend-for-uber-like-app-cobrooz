from __future__ import unicode_literals
from django.db import models

# Create your models here.

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=40, blank=False)
    email = models.EmailField()
    password = modals.Password()


