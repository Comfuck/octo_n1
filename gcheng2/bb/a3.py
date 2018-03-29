# coding:utf-8
import requests

import urllib3  # 使用这个方法就OK了
urllib3.disable_warnings()


url = "https://www.baidu.com"
r = requests.get(url, verify=False)
# print(r.encoding)  # 返回界面的编码格式
# print(r.url)
# print(r.status_code)
# print(r.headers)
# print(r.text)  # 文本格式
# # 字节方式输出
# print(r.content.decode("utf-8"))
print(r.text)