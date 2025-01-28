import os
from celery import Celery

from job_finder import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_finder.settings')

app = Celery('job_finder')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

celery_settings = {
    'beat_scheduler': 'django_celery_beat.schedulers.DatabaseScheduler',
    'task_always_eager': False,
    'result_backend': 'django-db',
}

app.conf.update(celery_settings)
