from django.apps import AppConfig


class HomeworksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.internship.homeworks'

    def ready(self):
        import apps.internship.homeworks.signals
