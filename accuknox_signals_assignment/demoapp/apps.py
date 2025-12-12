# demoapp/apps.py
from django.apps import AppConfig

class DemoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demoapp'

    def ready(self):
        # import signal handlers to register them
        from . import signals  # noqa
