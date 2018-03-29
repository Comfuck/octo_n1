# coding:utf-8

import requests
url = "http://www.cnblogs.com/yoyoketang/p/"
h = {  }  # 头部暂时不写
r = requests.get(url)
print(r.status_code)  # 状态码
print(r.headers)
print(r.text)







