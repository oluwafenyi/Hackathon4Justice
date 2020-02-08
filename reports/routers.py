
from rest_framework.routers import SimpleRouter

from .viewsets import ReportViewSet


router = SimpleRouter()
router.register(r'reports', ReportViewSet, basename='reports')
