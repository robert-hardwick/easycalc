import unittest 
from easycalc.calculators import calculate_infix
from easycalc.exceptions import InvalidExpressionException

class TestInfix(unittest.TestCase): 
  
    # Test Simple Addition  
    def test_addition(self):  
        ans = calculate_infix("1 + 2")
        self.assertEqual(ans, 3.0) 

    def test_subtract(self):  
        ans = calculate_infix("2 - 1")
        self.assertEqual(ans, 1.0) 

    def test_mul(self):  
        ans = calculate_infix("2 * 3")
        self.assertEqual(ans, 6.0) 

    def test_div(self):  
        ans = calculate_infix("1 / 2")
        self.assertEqual(ans, 0.5) 
    
    def test_invalid_format(self):
        # prefix notation
        self.assertRaises(InvalidExpressionException, calculate_infix, "+ 2 2")

    def test_invalid_format2(self):
        # trailing operand
        self.assertRaises(InvalidExpressionException, calculate_infix, "2 + 2 4")

    def test_precedence(self):  
        ans = calculate_infix("1 + 2 * 3")
        self.assertEqual(ans, 7.0) 

    def test_precedence2(self):  
        ans = calculate_infix("( 1 + 2 ) * 3")
        self.assertEqual(ans, 9.0) 

if __name__ == '__main__': 
    unittest.main() 