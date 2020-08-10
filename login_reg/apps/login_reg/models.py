from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name cannot be less than two characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name cannot be less than two characters"
        email = postData['email']
        if "@" not in email:
            errors['email'] = "Must be valid email"
        if ".com" not in email:
            errors['email'] = "Must be valid email"
        if len(postData['password']) < 4:
            errors['password'] = "Password must be at least 8 echaracters"
        return errors 

class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=25)
    objects = UserManager()

class Message(models.Model):
    message = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='comments')
    message = models.ForeignKey(Message, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    