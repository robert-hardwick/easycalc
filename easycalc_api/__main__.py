from flask import Flask, request, Response
from easycalc.calculators import calculate_infix, calculate_prefix
from easycalc.exceptions import InvalidExpressionException, InvalidOperatorException
from easycalc_api.response_handling import handle_bad_request, handle_exception, handle_unknown_exception, respond_success
import argparse

app = Flask(__name__)

calculator_dict = {
    "prefix" : calculate_prefix,
    "infix" : calculate_infix
}

@app.route('/<calculator>')
def calc(calculator):
    if calculator not in calculator_dict.keys():
        return bad_request()
    if 'expr' not in request.args:
        return bad_request()
    else:
        try:
            expr = request.args['expr']
            res = calculator_dict[calculator](expr)
            return respond_success(res)
        except (InvalidExpressionException, InvalidOperatorException) as e:
            return handle_exception(e)
        except Exception as e:
            return handle_unknown_exception()

def main():

    parser = argparse.ArgumentParser(prog='Prefix and Infix Web API')

    parser.add_argument('--port', type=int, help='Port to run calculator service', default=8888)    
    parsed_args = parser.parse_args()

    app.run(port=parsed_args.port)


if __name__ == "__main__":
    main()