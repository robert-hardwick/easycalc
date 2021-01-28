from enum import Enum, unique
from easycalc.core.exceptions import InvalidExpressionException, InvalidCalculatorException, InvalidOperatorException

# Response Handling
@unique
class ReturnCode(Enum):
    # success codes in range 1 to 20
    success = 1

    # start error codes
    # Http 401 codes
    error_bad_request = 21

    # Https 200 codes
    error_invalid_expression = 31
    error_invalid_operator = 32
    error_unknown = 33

# Lookup for error messages
return_code_to_message_dict = {
   ReturnCode.success: "",
   ReturnCode.error_bad_request: "Bad Request",
   ReturnCode.error_invalid_expression: "Invalid Expression",
   ReturnCode.error_invalid_expression: "Invalid Expression",
   ReturnCode.error_unknown: "Unknown Error Encountered"
}

def handle_response(return_code, data = None):
    """ Build a response and determine correct http code to use """
    if return_code.value <= 20:
        success = True
    else:
        success = False
    
    if return_code.value >= 21 and return_code.value <= 30:
        http_response_code = 401
    else:
        http_response_code = 200

    return {"success": success, "return_code": return_code.value, "message": return_code_to_message_dict[return_code], "data" : data }, http_response_code


def handle_exception(exception):
    if isinstance(exception, InvalidExpressionException):
        return handle_response(ReturnCode.error_invalid_expression)
    if isinstance(exception, InvalidOperatorException):
        return handle_response(ReturnCode.error_invalid_operator)
    else:
        return handle_response(ReturnCode.error_unknown)