import requests
def login(s,base_url,username="test",password="123456"):
    """
    登录
    :param s: 会话
    :param username: 用户名
    :param password: 密码
    :return: 返回接口响应
    """
    url = base_url+"/api/v1/login"
    body = {
        "username":username,
        "password":password
    }
    r = s.post(url,json = body)
    token = r.json()["token"]
    headers = {
        "Authorization": "Token %s" % token
    }
    s.headers.update(headers)
    return r
if __name__ == "__main__":
    base_url = "http://49.235.92.12:7005"
    s = requests.session()
    r = login(s,base_url=base_url)
    print(s.headers)
    print(r.status_code)