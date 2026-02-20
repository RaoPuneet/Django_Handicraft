from django.apps import AppConfig


class HandicraftappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'handicraftapp'

    def ready(self):
        import handicraftapp.signals