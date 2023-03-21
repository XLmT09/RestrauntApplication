# myapp/management/commands/update_field.py

from django.core.management.base import BaseCommand
from project.models import MenuItem

class Command(BaseCommand):
    def handle(self, *args, **options):
        # URL's for menu starters
        MenuItem.objects.filter(name = 'Chicken Taquitos').update(imgurl = 'https://i.postimg.cc/K8nnSp8C/Chicken-Taquitos.jpg')
        MenuItem.objects.filter(name = 'Nachos').update(imgurl = 'https://i.postimg.cc/HWJhfMfX/Nachos.jpg')
        MenuItem.objects.filter(name = 'Elote').update(imgurl = 'https://i.postimg.cc/fLCxJ8tk/Elote.jpg')
        MenuItem.objects.filter(name = 'Cheviche').update(imgurl = 'https://i.postimg.cc/c1fZ3PXv/Cheviche.jpg')
        MenuItem.objects.filter(name = 'Black Bean Salsa').update(imgurl = 'https://i.postimg.cc/tJdjHVY3/Black-Bean-Salsa.jpg')

        # URL's for menu mains
        MenuItem.objects.filter(name = 'Bean Salad').update(imgurl = 'https://i.postimg.cc/DfQk0Lws/Bean-Salad.jpg')
        MenuItem.objects.filter(name = 'Prawn Fajitas').update(imgurl = 'https://i.postimg.cc/HsXPLgWL/Prawn-Fajitas.jpg')
        MenuItem.objects.filter(name = 'Prawn Chirizo Quesadilla').update(imgurl = 'https://i.postimg.cc/bw992Y2m/Prawn-Chirizo-Quesadilla.jpg')
        MenuItem.objects.filter(name = 'King Prawn Taco').update(imgurl = 'https://i.postimg.cc/1Xpcyy0h/King-Prawn-Taco.jpg')
        MenuItem.objects.filter(name = 'Burrito').update(imgurl = 'https://i.postimg.cc/prMH7BXV/Burrito.jpg')

        #URL's for menu sides
        MenuItem.objects.filter(name = 'Black Beans and Rice').update(imgurl = 'https://i.postimg.cc/ncZxGTP0/Black-Beans-and-Rice.jpg')
        MenuItem.objects.filter(name = 'Salsa').update(imgurl = 'https://i.postimg.cc/Bbw71SL8/Salsa.jpg')
        MenuItem.objects.filter(name = 'Guacamole').update(imgurl = 'https://i.postimg.cc/133ZLXPF/Guacamole.jpg')
        MenuItem.objects.filter(name = 'Pozole').update(imgurl = 'https://i.postimg.cc/tTW0hVdK/Pozole.jpg')
        MenuItem.objects.filter(name = 'Tomato Avacado Salad').update(imgurl = 'https://i.postimg.cc/9QT4SLBK/Tomato-Avocado-Salad.jpg')

        #URL's for menu desserts
        MenuItem.objects.filter(name = 'Churros').update(imgurl = 'https://i.postimg.cc/t4vHybCM/Churros.jpg')
        MenuItem.objects.filter(name = 'Dulce de leche cheesecake').update(imgurl = 'https://i.postimg.cc/yYnMXK98/Dulce-de-leche-cheesecake.jpg')
        MenuItem.objects.filter(name = 'Sopapillas').update(imgurl = 'https://i.postimg.cc/9FJf4vQG/Sopapillas.jpg')
        MenuItem.objects.filter(name = 'Bunuelos').update(imgurl = 'https://i.postimg.cc/tC5jSW0y/Bunuelos.jpg')

        #URL's for menu drink
        MenuItem.objects.filter(name = 'Michelada').update(imgurl = 'https://i.postimg.cc/pT3n93VW/Michelada.jpg')
        MenuItem.objects.filter(name = 'Chamoyada').update(imgurl = 'https://i.postimg.cc/C1k6nsh8/Chamoyada.jpg')
        MenuItem.objects.filter(course = 'Drink', calories = 570).update(imgurl = 'https://i.postimg.cc/KjBWMSbx/Don-P-rignon-Brut-2003.jpg')
        MenuItem.objects.filter(name = 'Classic margarita').update(imgurl = 'https://i.postimg.cc/kM0wtpDh/Classic-margarita.jpg')
        MenuItem.objects.filter(name = 'Coke').update(imgurl = 'https://i.postimg.cc/t4xjNfzZ/Coke.jpg')
        MenuItem.objects.filter(name = 'Fanta').update(imgurl = 'https://i.postimg.cc/qM14jynn/Fanta.jpg')
        MenuItem.objects.filter(name = 'Paloma').update(imgurl = 'https://i.postimg.cc/vmpFgvn7/Paloma.jpg')