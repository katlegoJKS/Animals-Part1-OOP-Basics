from animal import Animal
from dog import Dog
from cat import Cat

class Home:
    
    def __init__(self,pets = []):
        self.pets = pets

    def adopt_pet(self,pet):
        for each_pet in self.pets:
            if each_pet == pet:
                raise Exception("You cannot adopt the same pet twice")
            self.pets.append(pet)

    def make_all_sounds():
        return dog1.food()

home = Home()
dog1 = Dog("Rax","barks")
cat1 = Cat("Stormy","meows")
home.adopt_pet(dog1)
home.adopt_pet(cat1)

print("Current pets: ")
print(home.pets)