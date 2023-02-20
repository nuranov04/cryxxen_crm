import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core', backend='redis://127.0.0.1:6379', broker='redis://127.0.0.1:6379')
app.conf.broker_url = "redis://127.0.0.1:6379"
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {!r}'.format(self.request))

# from __future__ import absolute_import, unicode_literals
