class Animal:

    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def food(self):
        print("{0} eats".format(self.name))


    def sounds(self):
        print("{0}".format(self.sound))


    
dog = Animal("Rax","Dog barks")

#dog.food()
#dog.sounds()

cat = Animal("Stormy","Cat meows")

#cat.food()
#cat.sounds()
