
from rest_framework import viewsets

from .models import Profile, CustomUser
from .serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
