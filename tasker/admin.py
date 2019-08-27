# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Task, Team, Comment, User

admin.site.register(Task)
admin.site.register(Team)
admin.site.register(Comment)
admin.site.register(User)
