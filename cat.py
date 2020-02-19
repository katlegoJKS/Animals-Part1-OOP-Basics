from animal import Animal

class Cat(Animal):

    def __init__(self,name,sound):
        super().__init__(name,sound)

    def eats(self):
        return self.name

    def sounds(self):
        return "Meow"

cat1 = Cat('','')
#print(cat1.eats())
#print(cat1.sounds())