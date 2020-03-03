import requests
from post import POST

url = "https://news.qq.com/zt2020/page/feiyan.htm?from=timeline&isappinstalled=0#/"
response = requests.get(url=url)

data = response.text

print(data)