import requests
import pytest

def test_get_my_ip():
    url = "https://uapis.cn/api/v1/network/myip"
    response = requests.get(url)
    assert response.status_code == 200
    json_data = response.json()
    assert "ip" in json_data

def test_wrong_url():
    url = "https://uapis.cn/api/v1/network/wrong_address"
    response = requests.get(url)
    assert response.status_code != 200