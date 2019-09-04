from django.db import models
from django.contrib.auth.models import AbstractUser
from dry_rest_permissions.generics import allow_staff_or_superuser, authenticated_users


class User(AbstractUser):
    pass


class Team(models.Model):
    name = models.CharField(max_length=72)
    creator = models.ForeignKey(User,
                                related_name='teammembers',
                                on_delete=models.CASCADE)
    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_write_permission(request):
        return False

    @allow_staff_or_superuser
    def has_write_permissions(self, request):
        return True

    created = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User,
                                   related_name='teammates')

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @allow_staff_or_superuser
    def has_write_permissions(self, request):
        return True


class Task(models.Model):
    name = models.CharField(max_length=500)
    creator = models.ForeignKey(User,
                                related_name='tasks',
                                on_delete=models.CASCADE)
    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @allow_staff_or_superuser
    def has_write_permission(self, request):
        return True

    description = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    teams = models.ManyToManyField(Team)
    finished = models.DateTimeField(auto_now_add=False,
                                    editable=True)


class Comment(models.Model):
    comment = models.TextField(blank=False)
    whencommented = models.DateTimeField(auto_now_add=True)
    whatcommented = models.ForeignKey(Task,
                                           related_name='commentfortask',
                                           on_delete=models.CASCADE,
                                           null=True)
    creator = models.ForeignKey(User,
                                    related_name='comments',
                                    on_delete=models.CASCADE)

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_write_permission(request):
        return True

    def has_object_write_permission(self, request):
        return request.user == self.creator


