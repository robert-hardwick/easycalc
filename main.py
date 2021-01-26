import sys
from easycalc.calculators import calculate_prefix, calculate_infix

import argparse
from enum import Enum

calculator_dict = {
    "prefix" : calculate_prefix,
    "infix" : calculate_infix
}

def main():

    parser = argparse.ArgumentParser(prog='Prefix/Infix Calculator')

    parser.add_argument('mode', type=str, choices=calculator_dict.keys(), help='Operation mode')
    parser.add_argument('sequence', type=str, help='Expression to parse (str)')
    

    parsed_args = parser.parse_args()
    mode = parsed_args.mode
    sequence = parsed_args.sequence

    result = calculator_dict[mode](sequence)
    print(result)

if __name__ == "__main__":
    main()