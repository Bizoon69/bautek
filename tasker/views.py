from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.object.all()

