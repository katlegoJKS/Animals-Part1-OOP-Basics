class Animal:

    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def eats(self):
        return "Food"


    def sounds(self):
        return self.sound


    
dog = Animal('Rax','barks')

#print(dog.eats())
#print(dog.sounds())

cat = Animal("Stormy","meows")

#print(cat.eats())
#print(cat.sounds())
