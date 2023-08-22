import requests

url = "https://fanyi.baidu.com/sug"

a= {
    "kw":input("请输入一个单词")
}

resp = requests.post(url,data=a)


print(resp.json())
input("按返回健退出:")