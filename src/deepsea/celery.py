import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deepsea.settings')

app = Celery('deepsea')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "check_teams_size": {
        'task': 'check_teams_size',
        'schedule': crontab(minute='*/5')
    },
}
