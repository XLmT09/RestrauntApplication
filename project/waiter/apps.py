from django.apps import AppConfig

# File for the app which is used to connect to the website, the class
# below will be the reference for the app under settings.py in projects folder
class WaiterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'waiter'
