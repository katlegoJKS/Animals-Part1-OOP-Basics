import unittest
from animal import Animal
from cat import Cat

class testAnimal(unittest.TestCase):

    def setUp(self):
        print('Pass')                               #If test is true then return Pass
        self.dog1 = Animal('Food','Bark')           #defines string to objects 'dog1' and 'cat1'
        self.cat1 = Animal('Food','Meow')

    def test_dog_sound(self):
        print('Does Dog bark')                      #Test question
        self.assertEqual(self.dog1.sound,'Bark')    #assert that the two arguments are equal to be true

    def test_dog_eats(self):
        print('Does Dog eat food')
        self.assertEqual(self.dog1.eat,'Food')

    def test_cat_sound(self):
        print("Does cat meow")
        self.assertEqual(self.cat1.sound,'Meow')

    def test_cat_eats(self):
        print('Does cat eat food')
        self.assertEqual(self.cat1.eat,'Food')

if __name__ == "__main__":
    unittest.main()
