from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Task(models.Model):
    name = models.CharField(max_length=500)
    creator = models.ForeignKey(User,
                                related_name='tasks',
                                on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    teammates = models.ManyToManyField(User)
    finished = models.DateTimeField(auto_now_add=True,
                                    editable=True)

class Team(models.Model):
    name = models.CharField(max_length=72)
    creator = models.ForeignKey(User,
                                related_name='teammembers',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User,
                              related_name='teammates')



class Comment(models.Model):
    comment = models.TextField(blank=False)
    commented = models.DateTimeField(auto_now_add=True)
    commentator = models.ForeignKey(User,
                                        related_name='comments',
                                        on_delete=models.CASCADE)




