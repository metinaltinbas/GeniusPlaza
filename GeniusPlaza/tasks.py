from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
from jobs.models import Job
import time
from datetime import datetime, timezone





@shared_task
def send_sms():
    d1 = datetime.now(timezone.utc)
    JobsObjects = Job.objects.filter(is_active=True,expire_date__lt=d1)
    for jobs in JobsObjects:
        jobs.is_active = False
        jobs.save()