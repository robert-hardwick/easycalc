import pytest
from easycalc.core.calculators import calculate_prefix
from easycalc.core.exceptions import InvalidExpressionException, InvalidOperatorException

# Test Simple Addition  
def test_addition():  
    assert calculate_prefix("+ 1 2") == 3.0

def test_subtract():  
    assert calculate_prefix("- 2 1") == 1.0

def test_mul():  
    assert calculate_prefix("* 2 3") == 6.0

def test_div():  
    assert calculate_prefix("/ 1 2") == 0.5

def test_nested_1():  
    assert calculate_prefix("+ 1 + 2 3") == 6.0

def test_nested_2():  
    assert calculate_prefix("+ + 1 1 + 2 3") == 7.0

# Test assertions

def test_invalid_operator(): 
    with pytest.raises(InvalidOperatorException):
        calculate_prefix("& 1 2")

def test_invalid_format():
    with pytest.raises(InvalidExpressionException):
        calculate_prefix("2 + 2")

def test_empty_expr():
    with pytest.raises(InvalidExpressionException):
        calculate_prefix("")

def test_no_operator():
    with pytest.raises(InvalidExpressionException):
        calculate_prefix("1 2")