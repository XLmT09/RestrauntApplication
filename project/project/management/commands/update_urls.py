# myapp/management/commands/update_field.py

from django.core.management.base import BaseCommand
from project.models import MenuItem

class Command(BaseCommand):
    def handle(self, *args, **options):
        # URL's for menu starters
        MenuItem.objects.filter(name = 'Chicken Taquitos').update(imgurl = 'https://drive.proton.me/urls/WQEAJ7N6D8#r4xpYnfCgFOg')
        MenuItem.obejcts.filter(name = 'Nachos').update(imgurl = 'https://drive.proton.me/urls/2EPT1Y71J8#oddAauKkfajp')
        MenuItem.obejcts.filter(name = 'Elote').update(imgurl = 'https://drive.proton.me/urls/G9C83QPSPW#4XR1jCZgCHVu')
        MenuItem.obejcts.filter(name = 'Cheviche').update(imgurl = 'https://drive.proton.me/urls/TA5GXZRCC0#E47ClL6sE6a8')
        MenuItem.obejcts.filter(name = 'Black Bean Salsa').update(imgurl = 'https://drive.proton.me/urls/2FHQ3TA15M#xcaOcnQdHOht')

        # URL's for menu mains
        MenuItem.obejcts.filter(name = 'Bean Salad').update(imgurl = 'https://drive.proton.me/urls/1H071CWTQR#uWOzzhM4HfxI')
        MenuItem.obejcts.filter(name = 'Prawn Fajitas').update(imgurl = 'https://drive.proton.me/urls/H9210X57RM#wxwy3QC0rJQB')
        MenuItem.obejcts.filter(name = 'Prawn Chirizo Quesadilla').update(imgurl = 'https://drive.proton.me/urls/3S9P2WZ1TM#ByLYhWP3zDzq')
        MenuItem.obejcts.filter(name = 'King Prawn Taco').update(imgurl = 'https://drive.proton.me/urls/3ZG76XQBXC#yosxnefXP6ll')
        MenuItem.obejcts.filter(name = 'Burrito').update(imgurl = 'https://drive.proton.me/urls/E2P74KH424#A6DvyZCsUIcN')