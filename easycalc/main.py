""" 
Easycalc Main Entrypoint for CLI and API
"""

from easycalc.core.calculators import valid_calculators, calculate
from easycalc.api import app
import click

@click.group()
def main():
  pass

@main.command(name="cli", context_settings=dict(
    ignore_unknown_options=True,
))
@click.argument('calculator', type=click.Choice(valid_calculators()))
@click.argument('expr', type=str)
def cli_cmd(calculator, expr):
    res = calculate(calculator, expr)
    print(res)

@main.command(name="api")
@click.option('--port', type=int, default=8888)
@click.option('--host', type=str, default='0.0.0.0')
def api_cmd(port, host):
    click.echo('Starting Easycalc API')
    app.run(port=port, host=host)

if __name__ == '__main__':
    main()