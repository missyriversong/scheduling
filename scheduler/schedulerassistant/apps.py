from django.apps import AppConfig


class SchedulerassistantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedulerassistant'

    def ready(self):
        import schedulerassistant.signals
    


