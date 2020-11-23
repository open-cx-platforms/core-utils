from django.apps import AppConfig


class DefaultConfig(AppConfig):
    name = 'core_utils'

    def ready(self):
        pass
