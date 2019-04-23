from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'User', views.UserViewSet)
router.register(r'Team', views.TeamViewSet)
router.register(r'Comment', views.CommentViewSet)
router.register(r'Task', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls))
]

