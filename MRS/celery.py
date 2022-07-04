from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MRS.settings')
app = Celery('MRS')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)

