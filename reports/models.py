
from django.conf import settings
from django.db import models


class Report(models.Model):
    PENDING = '1'
    SOLVED = '2'
    CANCELLED = '3'

    STATUSES = (
        (PENDING, 'Pending'),
        (SOLVED, 'Solved'),
        (CANCELLED, 'Cancelled')
    )

    title = models.CharField(max_length=200)
    case_description = models.TextField()
    reporter = models\
        .ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models\
        .CharField(choices=STATUSES, max_length=1, default=PENDING)
    image = models.ImageField(blank=True)