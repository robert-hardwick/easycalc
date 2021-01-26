
""" 
Custom exceptions module
"""

class InvalidExpressionException(Exception):
    
    def __init__(self, token = None, message="Unable to parse expression"):
        self.token = token
        self.message = message
        super().__init__(message)
    
    def __str__(self):
        if self.token is None:
            return self.message
        else:
            return "{} at token \'{}\'".format(self.message, self.token)

class InvalidOperatorException(Exception):

    def __init__(self, token, message="Invalid operator parsed"):
        self.token = token
        self.message = message
        super().__init__(message)
    
    def __str__(self):
        return "{} : \'{}\'".format(self.message, self.token)