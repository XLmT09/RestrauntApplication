# myapp/management/commands/update_field.py

from django.core.management.base import BaseCommand
from project.models import MenuItem

class Command(BaseCommand):
    def handle(self, *args, **options):
        MenuItem.objects.filter(name = 'Chicken Taquitos').update(imgurl = 'https://drive.proton.me/urls/WQEAJ7N6D8#r4xpYnfCgFOg')