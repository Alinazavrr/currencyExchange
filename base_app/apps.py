from django.apps import AppConfig


class BaseappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_app'

    def ready(self):
        from . import signals
