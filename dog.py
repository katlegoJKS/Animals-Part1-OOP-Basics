from animal import Animal

class Dog(Animal):

    def __init__(self,name,sound):
        super().__init__(name,sound)

    def eats(self):
        return "Food"

    def sounds(self):
        return "Bark"

dog1 = Dog('','')
#print(dog1.eats())
#print(dog1.sounds())