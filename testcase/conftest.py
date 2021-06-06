from api.login import login
import pytest
import requests
@pytest.fixture()
def login_fix(base_url):
    s = requests.session()
    login(s,base_url)
    return s