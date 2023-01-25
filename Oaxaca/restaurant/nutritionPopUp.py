from django.http import HttpResponse

class item:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
        
    def getName(self):
        return self.name
    
    def getCals(self):
        return "Calories : {0}".format(self.calories)
