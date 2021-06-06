import requests
import time
def register(base_url,username,password="123456"):
    url = base_url+"/api/v1/register"
    time_data= str(int(time.time()*100))
    email = time_data+"@qq.com"
    body ={
        "username":username,
        "password":password,
        "email":email
    }
    r = requests.post(url,json=body)
    return r
if __name__ == "__main__":
    base_url = "http://49.235.92.12:7005"
    r = register(base_url,"layzhang91982")
    print(r.json())