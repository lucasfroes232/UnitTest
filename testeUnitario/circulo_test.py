import unittest 
from circulo import Circle
class testCircle(unittest.TestCase):

    def setUp(self):
        self.circ= Circle(5)

    def test_constructor(self):
        self.assertEqual(self.circ.radius,5)
    
    def test_area(self):
       self.assertEqual(self.circ.area(),78.5)
    
    def test_circum(self):
        self.assertEqual(self.circ.circumference(),31.400000000000002)
    
if __name__ =='__main__':
    unittest.main()