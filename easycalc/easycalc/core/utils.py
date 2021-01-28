
""" 
Common utils
"""

import operator
from easycalc.core.exceptions import InvalidOperatorException

operator_dict = {
    '+' : ( operator.add, 2 ),
    '-' : ( operator.sub, 2 ),
    '*' : ( operator.mul, 3 ),
    '/' : ( operator.truediv, 3 )
}

def get_operator(operator : str):
    """ Get operator from char """
    if is_operator(operator):
        return operator_dict[operator][0]
    else:
        raise InvalidOperatorException(operator)

def is_operator(operator : str):
    """ Returns true if 'operator' char is valid operator """
    return operator in operator_dict.keys()

def get_operator_precendence(operator : str):
    """ Returns operator precedence from char """
    if is_operator(operator):
        return operator_dict[operator][1]
    else:
        raise InvalidOperatorException(operator)