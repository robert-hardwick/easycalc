import sys
from easycalc.calculators import calculate_prefix, calculate_infix

import argparse
from enum import Enum

calculator_dict = {
    "prefix" : calculate_prefix,
    "infix" : calculate_infix
}

def main():

    parser = argparse.ArgumentParser(prog='Prefix and Infix Calculator')

    parser.add_argument('calculator', type=str, choices=calculator_dict.keys(), help='Operation mode')
    parser.add_argument('expression', type=str, help='Expression to parse (str)')
    
    parsed_args = parser.parse_args()

    # parse the expression on the specified calculator
    result = calculator_dict[parsed_args.calculator](parsed_args.expression)
    print(result)

if __name__ == "__main__":
    main()