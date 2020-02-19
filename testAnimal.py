import unittest
from animal import Animal

class testAnimal(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.dog1 = Animal('Food','Bark')
        self.cat1 = Animal('Food','Meow')

    def test_dog_sound(self):
        print('test sound')
        self.assertEqual(False,self.dog1.sounds == 'Bark')

    def test_dog_eats(self):
        self.assertEqual(False,self.dog1.eats == 'Food')

    def test_cat_sound(self):
        self.assertEqual(False,self.cat1.sounds == 'Meow')

    def test_cat_eats(self):
        self.assertEqual(False,self.cat1.eats == 'Food')

if __name__ == "__main__":
    unittest.main()
