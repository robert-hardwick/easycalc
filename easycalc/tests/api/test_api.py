import pytest
import flask
import json
from easycalc.api import app as flask_app
from easycalc.api.response import ReturnCode


@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

# Test Bad Requests

def test_bad_command(app, client):
    res = client.get('/invalid')
    assert res.status_code == 401
    expected_rc = ReturnCode.error_bad_request.value
    assert expected_rc == json.loads(res.get_data(as_text=True))["return_code"]

def test_no_expression(app, client):
    res = client.get('/prefix')
    assert res.status_code == 401
    expected_rc = ReturnCode.error_bad_request.value
    assert expected_rc == json.loads(res.get_data(as_text=True))["return_code"]

# Test Valid Requests

def test_valid_prefix(app, client):
    res = client.get('/prefix?expr=%2B%202%201')
    assert res.status_code == 200
    expected_rc = ReturnCode.success.value
    assert expected_rc == json.loads(res.get_data(as_text=True))["return_code"]
    expected_data = 3.0
    assert expected_data == json.loads(res.get_data(as_text=True))["data"]

def test_valid_infix(app, client):
    res = client.get('/infix?expr=2%20%2B%202')
    assert res.status_code == 200
    expected_rc = ReturnCode.success.value
    assert expected_rc == json.loads(res.get_data(as_text=True))["return_code"]
    expected_data = 4.0
    assert expected_data == json.loads(res.get_data(as_text=True))["data"]