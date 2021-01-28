from easycalc.core import utils
from easycalc.core.exceptions import InvalidExpressionException

# Test Simple Addition  
def test_is_operator():  
    assert utils.is_operator("+") == True

def test_invalid_operator():  
    assert utils.is_operator("&") == False