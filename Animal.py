class Animal:
    def __init__(self, eats,sound):
        self.eats = eats
        self.sound = sound


class Dog(Animal):
        def eat(self):
            return "Dogmore"
        def sounds(self):
            return 'Barks'


class Cat(Animal):
        def eat(self):
            return "CatMore"
        def sounds(self):
            return 'Meows'


class Home:
    def __init__(self,pet,name,eats,sound):
        self.pet = pet
        self.name = name
        self.petID = Animal(eats,sound)
    def adoptPet(self,petName):
        self.petName = ["Dog", "Cat"]
        self.petName.append(input("Enter pet name: "))
        print(petName)
    def makeAllSounds(self):
        pass



d = Dog(' ',' ')
c = Cat(' ',' ')
h = Home(' ',' ',' ',' ')

print("Dog eats",d.eat(),"and",d.sounds())
print("Cat eats",c.eat(),"and",c.sounds())
print(h.adoptPet(""))