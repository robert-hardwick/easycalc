import unittest 
from easycalc.calculators import calculate_prefix
from easycalc.exceptions import InvalidExpressionException, InvalidOperatorException

class TestPrefix(unittest.TestCase): 
  
    # Test Simple Addition  
    def test_addition(self):  
        ans = calculate_prefix("+ 1 2")
        self.assertEqual(ans, 3.0) 

    def test_subtract(self):  
        ans = calculate_prefix("- 2 1")
        self.assertEqual(ans, 1.0) 

    def test_mul(self):  
        ans = calculate_prefix("* 2 3")
        self.assertEqual(ans, 6.0) 

    def test_div(self):  
        ans = calculate_prefix("/ 1 2")
        self.assertEqual(ans, 0.5) 
    
    def test_nested_1(self):  
        ans = calculate_prefix("+ 1 + 2 3")
        self.assertEqual(ans, 6.0) 

    def test_nested_2(self):  
        ans = calculate_prefix("+ + 1 1 + 2 3")
        self.assertEqual(ans, 7.0) 

    def test_invalid_operator(self):  
        self.assertRaises(InvalidOperatorException, calculate_prefix, "& 1 2") 

    def test_invalid_format(self):
        self.assertRaises(InvalidExpressionException, calculate_prefix, "2 + 2") 

    def test_empty_expr(self):  
        self.assertRaises(InvalidExpressionException, calculate_prefix, "") 

    def test_no_operator(self):  
        self.assertRaises(InvalidExpressionException, calculate_prefix, "1 2") 

if __name__ == '__main__': 
    unittest.main() 