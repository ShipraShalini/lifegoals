from __future__ import absolute_import, unicode_literals

import os
from celery import Celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lifegoals.settings')


task_queue = Celery(str("wolfe"))

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
task_queue.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django janus configs.
task_queue.autodiscover_tasks()


@task_queue.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
