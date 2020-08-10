from __future__ import unicode_literals
from django.db import models


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['show_title']) < 0:
            errors["show_title"] = "Please enter a proper show title"
        if len(postData['show_network']) < 0:
            errors["show_network"] = "Must enter a correct network"
        if len(postData['show_release']) < 0:
            errors["show_release"] - "Must enter a valid date"
        return errors 

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

