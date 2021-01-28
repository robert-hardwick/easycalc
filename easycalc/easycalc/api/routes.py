from easycalc.api import app
from easycalc.core.calculators import calculate
from easycalc.api.response import handle_response, handle_exception, ReturnCode
from flask import request

def calc(calculator):
    """ Flask route/entrypoint for API at /"""
    if 'expr' not in request.args:
        return handle_response(ReturnCode.error_bad_request)
    else:
        try:
            expr = request.args['expr']
            res = calculate(calculator, expr)
            return handle_response(ReturnCode.success, data=res)
        except Exception as e:
            return handle_exception(e)

@app.route('/infix')
def infix_calc():
    """ Flask route/entrypoint for API at /"""
    return calc("infix")

@app.route('/prefix')
def prefix_calc():
    """ Flask route/entrypoint for API at /"""
    return calc("prefix")