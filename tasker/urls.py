from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'user', views.UserViewSet) #urlsy z malej nie z duzej, zawsze i wszedzie
router.register(r'team', views.TeamViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'task', views.TaskViewSet)


urlpatterns = [
    path('', include(router.urls))
]