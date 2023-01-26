from django.http import HttpResponse

class item:
    def __init__(self,name,calories,ingredients,price,alergies,courses):
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.alergies = alergies
        self.courses = courses
        self.calories = calories
        
    def getName(self):
        return self.name
    
    def getCals(self):
        return self.calories
    
    def getIngredients(self):
        return self.ingredients
    
    def getPrice(self):
        return self.price
    
    def getCourse(self):
        return self.courses
    
    def getAlergies(self):
        return self.alergies
