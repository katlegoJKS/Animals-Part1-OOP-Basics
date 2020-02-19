class Animal:

    def __init__(self,eat,sound):
        self.eat = eat
        self.sound = sound

    def eats(self):
        return self.eat


    def sounds(self):
        return self.sound


    
dog = Animal('Rax','barks')

#print(dog.eats())
print("dog",dog.sounds())

cat = Animal("Stormy","meows")

#print(cat.eats())
print("cat",cat.sounds())
print('')

