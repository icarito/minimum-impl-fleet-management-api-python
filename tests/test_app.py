import pytest
from .mock_data import TAXIS_RESPONSE;
import requests
from unittest.mock import patch
from fleet_api.controllers.TaxiController import getTaxis

def test_to_api():
    response = requests.get("http://localhost:5000/taxis") //postman 
    content = response.json()
    print(content)
    assert response.status_code == 200
    assert len(content['taxis']) == 1


def test_no_http()
    response = getTaxis()



""" @patch('fleet_api.app.getTaxis',
    name='mock_get_taxis',
    return_value=TAXIS_RESPONSE)
def test_to_mock(mocked_get):
    response = requests.get("http://localhost:5000/taxis")
    
    content = response.json()
    assert mocked_get.called
    assert response.status_code == 200
    assert len(content['taxis']) == 3 """