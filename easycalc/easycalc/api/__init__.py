from flask import Flask, request
from easycalc.core.calculators import calculate, valid_calculators
from easycalc.api.response import handle_response, handle_exception, ReturnCode

app = Flask(__name__)

@app.route('/<calculator>')
def calc(calculator):
    """ Flask route/entrypoint for API at /"""
    if calculator not in valid_calculators() or 'expr' not in request.args:
        return handle_response(ReturnCode.error_bad_request)
    else:
        try:
            expr = request.args['expr']
            res = calculate(calculator, expr)
            return handle_response(ReturnCode.success, data=res)
        except Exception as e:
            return handle_exception(e)

def start(port, host):
    app.run(port=port, host=host)