""" 
Easycalc Main Entrypoint for CLI and API
"""

from easycalc.core.calculators import valid_calculators, calculate
from easycalc import api
import click

@click.group()
def main():
  pass

@main.command(name="cli")
@click.argument('calculator', type=str)
@click.argument('expr', type=str)
def cli_cmd(calculator, expr):
    res = calculate(calculator, expr)
    print(res)

@main.command(name="api")
@click.option('--port', type=int, default=8888)
@click.option('--hostname', type=str, default='0.0.0.0')
def api_cmd(port, hostname):
    click.echo('Starting Easycalc API')
    api.start(port, hostname)

if __name__ == '__main__':
    main()