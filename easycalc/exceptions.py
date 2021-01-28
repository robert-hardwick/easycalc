
""" 
Custom exceptions module
"""

class InvalidExpressionException(Exception):
    
    def __init__(self, message="Unable to parse expression"):
        super().__init__(message)
    

class InvalidOperatorException(Exception):

    def __init__(self, message="Invalid operator parsed"):
        super().__init__(message)
    