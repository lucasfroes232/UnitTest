import unittest 
from person import Person
class testPerson(unittest.TestCase):

    def setUp(self):
        self.person= Person("lucas",20)

    def test_constructor(self):
        self.assertEqual(self.person.name,"lucas")
        self.assertEqual(self.person.age,20)
    
    def test_update_age(self):
        self.person.update_age(35)
        self.assertEqual(self.person.age, 35)
        
    def test_adult(self):
        self.assertTrue(self.person.is_adult(18))
    
if __name__ =='__main__':
    unittest.main()