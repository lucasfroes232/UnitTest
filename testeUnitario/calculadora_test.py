import unittest 
from calculadora import Calculadora
class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora(5,3)

    def test_constructor(self):
        self.assertEqual(self.calc.n1,5)
        self.assertEqual(self.calc.n2,3)
    
    def test_som(self):
       self.assertEqual(self.calc.soma(),8)
    
    def test_sub(self):
        self.assertEqual(self.calc.subtrai(),2)
    
    def test_mult(self):
        self.assertEqual(self.calc.multiplica(),15)
    
    def test_div(self):
        self.assertEqual(self.calc.divide(),1.6666666666666667)

if __name__ =='__main__':
    unittest.main()