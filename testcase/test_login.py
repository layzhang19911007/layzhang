import pytest
import requests
from api.login import login
from config.conftest import root_path
from common.read_yml import read_yml
import os
yml_path = os.path.join(root_path,"data","test_login.yml")
test_data = read_yml(yml_path)
print("输出测试数据：",test_data)
@pytest.mark.parametrize("test_input,expected",test_data)
def test_login_case(test_input,base_url,expected):
    print(base_url)
    s = requests.session()
    r = login(s,base_url,test_input["username"],test_input["password"])
    print(base_url)
    print(r.json())
    assert r.json()["code"] == expected["code"]
    assert r.json()["msg"] == expected["msg"]