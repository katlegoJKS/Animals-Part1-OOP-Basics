from animal import Animal

class Dog(Animal):

    def __init__(self,eat,sound):
        super().__init__(eat,sound)

    def food(self):
        print(self.eat + " eats")

    def sounds(self):
        print(self.sound + "barks")

dog1 = Dog("Rax","Dog ")
dog1.food()
dog1.sounds()