
from rest_framework import serializers

from .models import Report


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'case_description', 'reporter',
                  'status', 'image')
        model = Report
