
from rest_framework import viewsets

from .serializers import ReportSerializer
from .models import Report


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
