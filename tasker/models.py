from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=72)
    created = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name = models.CharField(max_length=72)
    creator = models.ForeignKey(AbstractUser,
                                related_name='stary',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

class Task(models.Model):
    name = models.CharField(max_length=500)
    creator = models.ForeignKey(User,
                                related_name='tasks',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(auto_now=True)

class Team(models.Model):
    name = models.CharField(max_length=72)
    creator = models.ForeignKey(User,
                                related_name='teammembers',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User,
                              related_name='teammates',
                              on_delete=models.CASCADE)

class Comment(models.Model):
    comment = models.TextField(blank=False)
    commented = models.DateTimeField(auto_now_add=True)
    who_commented = models.ForeignKey(User,
                                           related_name='comments',
                                           on_delete=models.CASCADE)




