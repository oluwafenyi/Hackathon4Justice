
from rest_framework import viewsets
from rest_framework import permissions

from freedeon.permissions import IsReporterOrReadOnly
from .serializers import ReportSerializer
from .models import Report


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    permission_classes = [IsReporterOrReadOnly]
    permission_classes_by_action = {
        'create': [permissions.IsAuthenticatedOrReadOnly],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in
                    self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
