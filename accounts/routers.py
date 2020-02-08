
from rest_framework.routers import SimpleRouter

from .viewsets import UserViewset


router = SimpleRouter()
router.register(r'users', UserViewset)
