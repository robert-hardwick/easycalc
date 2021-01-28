from flask import Flask

app = Flask(__name__)

from easycalc.api import routes