import pytest
from easycalc.core.calculators import calculate_infix
from easycalc.core.exceptions import InvalidExpressionException
  
# Test Simple Addition  
def test_addition():  
    assert calculate_infix("1 + 2") == 3.0 

def test_subtract():  
    assert calculate_infix("2 - 1") == 1.0

def test_mul():  
    assert calculate_infix("2 * 3") == 6.0

def test_div():  
    assert calculate_infix("1 / 2") == 0.5

def test_invalid_format():
    # prefix notation
    with pytest.raises(InvalidExpressionException):
        calculate_infix("+ 2 2")

def test_invalid_format2():
    # trailing operand
     with pytest.raises(InvalidExpressionException):
         calculate_infix("2 + 2 4")

def test_precedence():  
    assert calculate_infix("1 + 2 * 3") == 7.0

def test_precedence2():  
    assert calculate_infix("( 1 + 2 ) * 3") == 9.0