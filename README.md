# Easycalc - Prefix and Infix Calculator

Simple Infix and Prefix calculator and Flask-based web api.

## Setup

    $ git clone https://github.com/robert-hardwick/easycalc.git
    $ cd easycalc/easycalc
    $ python -m pip install -r requirements.txt

## Basic Usage

The standalone CLI and Web API use the same invocation script (main.py).

### Standalone CLI

To run command line

    $ python main.py cli 'prefix|infix' expr

Example

    $ python main.py cli prefix "+ 1 1"

### Web API

Run API server directly

    $ python main.py api --port <PORT> (default = 8888)

Run containerized web service

    $ cd </path/to/repo/root>
    $ sh ./start_service.sh

Use curl to send some requests

\+ 1 1 :

    $ curl http://127.0.0.1:8888/prefix?expr=%2B%201%201
    response =
    {"code":null,"data":2.0,"message":null,"success":true}

3 \* 2 :

    $ curl http://127.0.0.1:8888/infix?expr=3%20%2A%202
    response =
    {"code":null,"data":6.0,"message":null,"success":true}

Some invalid requests

Unescaped html:

    $ curl http://127.0.0.1:8888/infix?expr=3*2
    response =
    {"code":2,"data":null,"message":"Invalid Operator Encountered","success":false}


Invalid url:

    $ curl curl http://127.0.0.1:8888/somethingelse
    response = 
    {"code":null,"data":null,"message":"Bad request","success":false}

## Run Tests

Install pytest

    $ python -m pip install pytest

Run tests

    $ python -m pytest tests