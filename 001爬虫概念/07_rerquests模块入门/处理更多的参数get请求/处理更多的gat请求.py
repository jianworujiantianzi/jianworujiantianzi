import requests

url = "https://movie.douban.com/j/chart/top_list"

canshu = {
    "type": "13",
    "interval_id": "100:90",
    "action":"",
    "start":"0",
    "limit":"20"
}
#处理一个小小的反爬
headars = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"

}

resp = requests.get(url,params=canshu,headers=headars)

#print(resp.text)  #返回的还是json数据
#print(resp.request.url)  #查看url
print(resp.json())