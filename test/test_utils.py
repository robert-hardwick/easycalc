import unittest 
from easycalc import utils
from easycalc.exceptions import InvalidExpressionException

class TestUtils(unittest.TestCase): 
  
    # Test Simple Addition  
    def test_is_operator(self):  
        self.assertTrue(utils.is_operator("+"))

    def test_invalid_operator(self):  
        self.assertFalse(utils.is_operator("&")) 

if __name__ == '__main__': 
    unittest.main() 