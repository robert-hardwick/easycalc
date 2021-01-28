

def respond_success(result):
    return {"success": True, "message": None, "data" : result, "code": None}, 200

def respond_failure(message, error_code=None):
    return {"success": False, "message": message, "data" : None, "code": error_code}, 200

def bad_request():
    return {"success": False, "message": "Bad request", "data" : None, "code": None}, 400

def handle_exception(exception):
    if isinstance(exception, InvalidExpressionException):
        respond_failure("Invalid Expression", 1)
    if isinstance(exception, InvalidOperatorException):
        return respond_failure("Invalid Operator Encountered", 2)
    else:
        return handle_unknown_exception()

def handle_unknown_exception():
    return respond_failure("Unknown exception encountered", 0)