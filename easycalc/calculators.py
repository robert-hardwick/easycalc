
""" 
Prefix and Infix expression calculation algorithms
"""

from easycalc.utils import get_operator, is_operator, get_operator_precendence
from easycalc.exceptions import InvalidExpressionException, InvalidOperatorException

def calculate_prefix(expr):
    """Performs calculation of prefix expression

    Parameters
    ----------
    expr : str
        Prefix expression to be calculated

    Returns
    -------
    float
        result of prefix calculation
    """

    if expr == "":
        raise InvalidExpressionException()

    tokens = expr.split(" ")

    operand_stack = []
    
    for token in reversed(tokens):

        if token.isnumeric():
            operand_stack.append(float(token))
        elif is_operator(token):

            # there must be at least 2 values in operand_stack
            if len(operand_stack) < 2:
                raise InvalidExpressionException(token)

            # pop the operands from the operand_stack in the correct order
            left = operand_stack.pop()
            right = operand_stack.pop()
            
            # add new current total to operand_stack
            operand_stack.append(get_operator(token)(left, right))
        else:
            raise InvalidOperatorException(token)

    # operand_stack should be reduced to 1 at this point
    if len(operand_stack) > 1:
        raise InvalidExpressionException()

    return operand_stack.pop()

def calculate_infix(expr):
    """Performs calculation of infix expression
    Implementation based on shunting-yard algorithm ( https://en.wikipedia.org/wiki/Shunting-yard_algorithm)

    Parameters
    ----------
    expr : str
        Infix expression to be calculated

    Returns
    -------
    float
        result of infix calculation
    """
    if expr == "":
        raise InvalidExpressionException()

    tokens = expr.split(" ")

    operator_stack = []
    operand_stack = []

    def _evaluate_stack():
        """ Helper method to evaluate the operand_stack  """
        # right operand is popped first
        right = operand_stack.pop()
        left = operand_stack.pop()
        operator = operator_stack.pop()
        
        operand_stack.append(get_operator(operator)(left, right))

    for token in tokens:

        # if token is opening brace push it to operations stack
        if token == '(':
            operator_stack.append(token)

        elif token.isnumeric():
            operand_stack.append(float(token))
        
        # if token is closing brace then solve the equation
        elif token == ')':

            while len(operator_stack) > 0 and operator_stack[-1] != "(":
                _evaluate_stack()
            operator_stack.pop()

        elif is_operator(token):

            # operand_stack cannot be empty
            if len(operand_stack) == 0:
                raise InvalidExpressionException()

            while len(operator_stack) > 0 and is_operator(operator_stack[-1]) and get_operator_precendence(operator_stack[-1]) >= get_operator_precendence(token):
                _evaluate_stack()

            operator_stack.append(token)

        else:
            raise InvalidOperatorException(token)

    while len(operator_stack) > 0:
        _evaluate_stack()
    
    # operand_stack should be reduced to 1 at this point
    if len(operand_stack) > 1:
        raise InvalidExpressionException()

    return operand_stack[-1]