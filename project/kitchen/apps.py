from django.apps import AppConfig

# This is the file for the app which is used to connect to the website, the class
# below will be the reference for the app under settings.py in projects folder
class KitchenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kitchen'
