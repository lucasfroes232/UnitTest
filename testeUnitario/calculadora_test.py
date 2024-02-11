import unittest 
from calculadora import Calculadora
class testCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()
    
    def test_som(self):
       self.assertEqual(self.calc.soma(5,3),8)
    
    def test_sub(self):
        self.assertEqual(self.calc.subtrai(5,3),2)
    
    def test_mult(self):
        self.assertEqual(self.calc.multiplica(5,3),15)
    
    def test_div(self):
        self.assertEqual(self.calc.divide(5,3),1.6666666666666667)

if __name__ =='__main__':
    unittest.main()
