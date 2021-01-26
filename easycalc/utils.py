import operator
from easycalc.exceptions import InvalidOperatorException

ops = {
    '+' : ( operator.add, 2 ),
    '-' : ( operator.sub, 2 ),
    '*' : ( operator.mul, 3 ),
    '/' : ( operator.truediv, 3 )
}

def get_operator(operator):
    if is_operator(operator):
        return ops[operator][0]
    else:
        raise InvalidOperatorException(operator)

def is_operator(operator):
    return operator in ops.keys()

def get_operator_precendence(operator):
    if is_operator(operator):
        return ops[operator][1]
    else:
        raise InvalidOperatorException(operator)