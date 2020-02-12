class Animal:

    def __init__(self,eat,sound):
        self.eat = eat
        self.sound = sound

    def food(self):
        print("{0} eats".format(self.eat))


    def sounds(self):
        print("{0}".format(self.sound))


    
dog = Animal("Rax","Dog barks")

#dog.food()
#dog.sounds()

cat = Animal("Stormy","Cat meows")

#cat.food()
#cat.sounds()
