
from rest_framework import viewsets

from freedeon import permissions
from .models import Profile, CustomUser
from .serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthUserOrReadOnly]
    permission_classes_by_action = {
        'list': [permissions.IsAdmin]
    }

    def get_permissions(self):
        try:
            return [permission() for permission in
                    self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
