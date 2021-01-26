
from easycalc.utils import get_operator, is_operator, get_operator_precendence
from easycalc.exceptions import InvalidExpressionException

def calculate_prefix(expr):

    eval_stack = []

    for token in reversed(expr):

        if token.isnumeric():
            eval_stack.append(float(token))
        elif is_operator(token):
            left = eval_stack.pop()
            right = eval_stack.pop()
            
            eval_stack.append(get_operator(token)(left, right))
        else:
            raise InvalidExpressionException("Invalid value in sequence")

    return eval_stack.pop()

# use shunting yard algorithm
def calculate_infix(expr):

    operator_stack = []
    value_stack = []

    for token in expr:

        # if token is opening brace push it to operations stack
        if token == '(':
            operator_stack.append(token)

        elif token.isnumeric():
            value_stack.append(float(token))
        
        # if token is closing brace then solve the equation
        elif token == ')':

            while len(operator_stack) > 0 and operator_stack[-1] != "(":
                left = value_stack.pop()
                right = value_stack.pop()
                operator = operator_stack.pop()
                
                value_stack.append(get_operator(operator)(left, right))

            # pop the opening brace
            operator_stack.pop()
        elif is_operator(token):
            while len(operator_stack) > 0 and is_operator(operator_stack[-1]) and get_operator_precendence(operator_stack[-1]) >= get_operator_precendence(token):

                left = value_stack.pop()
                right = value_stack.pop()
                operator = operator_stack.pop()
                
                value_stack.append(get_operator(operator)(left, right))

            operator_stack.append(token)

        else:
            raise InvalidExpressionException("Invalid value in sequence")

    while len(operator_stack) > 0:
        left = value_stack.pop()
        right = value_stack.pop()
        operator = operator_stack.pop()
        
        value_stack.append(get_operator(operator)(left, right))

    return value_stack[-1]