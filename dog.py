from animal import Animal

class Dog(Animal):

    def __init__(self,name,sound):
        super().__init__(name,sound)

    def food(self):
        print(self.name + " eats")

    def sounds(self):
        print(self.sound + "barks")

dog1 = Dog("Rax","Dog ")
dog1.food()
dog1.sounds()