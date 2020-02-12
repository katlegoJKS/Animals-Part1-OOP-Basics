from animal import Animal

class Cat(Animal):

    def __init__(self,eat,sound):
        super().__init__(eat,sound)

    def food(self):
        print(self.eat + " eats")

    def sounds(self):
        print(self.eat + "meows")

cat1 = Cat("Stormy ","")
cat1.food()
cat1.sounds()