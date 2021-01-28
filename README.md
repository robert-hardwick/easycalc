# Easycalc - Prefix and Infix Calculator

Simple Infix and Prefix calculator.

## easycalc

library and standalone command-line app

### Setup

    $ python -m pip install -r easycalc/requirements.txt

### Basic Usage

To run command line

    $ python -m easycalc 'prefix|infix' expr

To run tests

    $ python -m unittest easycalc.tests

## easycalc-api

Flask-based web service for easycalc

### Setup

    $ python -m pip install -r easycalc-api/requirements.txt

### Basic Usage

To start the web api

    $ python -m easycalc-api (Optional) --port <PORT>

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

To run tests

    $ python -m unittest easycalc-api.tests