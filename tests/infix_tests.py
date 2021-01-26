import unittest 
from picalc.calculators.prefix_calc import PrefixCalculator

class InfixTests(unittest.TestCase): 
  
    # Test Simple Addition  
    def test_addition(self):  
        calculator = PrefixCalculator()
        ans = calculator.calculate(["+", "1", "2"])
        self.assertEqual(ans, 3.0) 

    def test_subtract(self):  
        calculator = PrefixCalculator()
        ans = calculator.calculate(["-", "2", "1"])
        self.assertEqual(ans, 1.0) 

    def test_mul(self):  
        calculator = PrefixCalculator()
        ans = calculator.calculate(["*", "2", "3"])
        self.assertEqual(ans, 6.0) 

    def test_div(self):  
        calculator = PrefixCalculator()
        ans = calculator.calculate(["\\", "2", "2"])
        self.assertEqual(ans, 2.0) 
    
    def test_invalid_format(self):
        calculator = PrefixCalculator()
        self.assertRaises(ValueError, calculator.calculate, ["2", "+", "2"]) 




if __name__ == '__main__': 
    unittest.main() 