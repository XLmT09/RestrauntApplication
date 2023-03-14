from django.apps import AppConfig

class MainAppConfig(AppConfig):
    name = 'project'
    def ready(self):
        print("START UP CODE")


class ManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'


class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'