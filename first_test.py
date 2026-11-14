from urllib import response

import requests

url = "http://uapis.cn/api/v1/network/myip"

r = requests.get(url)

print(r.text)

if r.status_code == 200:
    print("测试通过")
else:
    print("测试失败")

if "ip" in r.text:
    print("测试通过")
else:
    print("测试失败")