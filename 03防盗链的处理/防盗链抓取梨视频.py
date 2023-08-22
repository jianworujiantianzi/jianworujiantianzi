""""""
"""
思路
    1.拿到contId
    2.拿到videosStatus返回的json. -> srcURL
    3.srcURL里面的内容进行修整
    4.下载视频
"""
import requests

"""第一步准备原始的url"""
url = "https://www.pearvideo.com/video_1078077"
"""
根据之前的分析这个后面的那是个数再后面有很大的用处所以要先把它拆出来
因为要的数据刚好是第一个所以就在后面加一个列表里面写一个1就是只提取第一个数据
"""
contId = url.split("_")[1]
"""打印一下看看要的数据提取的有没有问题"""
# print(contId)
"""这个网页就是再浏览器里面点开要拿数据的那个网页用浏览器工具F12里面的url直接复制过来就可"""
videosStatusURL = "https://www.pearvideo.com/videoStatus.jsp?contId=1078077&mrd=0.985132020"
"""从上面这个网址里面可以拿到一点大堆的东西"""
headers = {
    #模拟浏览器操作
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    #防盗链：溯源，当前本次请求的上一级是谁
    "Referer":"https://www.pearvideo.com/video_1078077"
}
"""去请求那个网页 然后headers里面传入反爬的一些对策比如模拟人的操作和一些防盗链"""
resp = requests.get(videosStatusURL,headers=headers)
"""这个给出的结果不好拿东西用下面的json给出的是一个字典类的东西比较好找东西"""
# print(resp.json())
dic = resp.json()
"""查看一下字典有没有问题"""
# print(dic)
"""
再preview里面一层一层的找找到srcUrl
如果理解不透的话就是浏览器工具里面的F12Network里面XHR工具里面的再preview再里面一层一层的找找到最后的
srcUrl对应的值
"""
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
"""
这个是查找systemTime后面的哪一个数字跟上一步要查找的东西放在一个字典里面这个要单独的列举出来
后面能够用的到
"""
systemTime = dic["systemTime"]
# print("原网址",srcUrl)
# print("要改的那个数",systemTime)
"""利用字符串替换的方法把原来的systemTime替换成cont-{contId}因为只有把里面的那个systemTime改成
cont-加上原网站后面的那个数才是有效的一个网址   这样才能进行访问
"""
srcUrl = srcUrl.replace(systemTime,f"cont-{contId}")
print(srcUrl)

"""
下载视频
首先先打开准备一个文件因为是视频所以后缀是.mp4   他的模式为wb
"""
with open("a.mp4",mode="wb") as f:
    f.write(requests.get(srcUrl).content)

"""
# with open("a.mp4" ,mode="wb") as f
这行代码使用with语句打开一个名为"a.mp4"的文件
，并以二进制写入模式（"wb"）打开。with语句用于处理文件对象，它可以确保文件正确关闭
，即使在处理文件时出现异常。在这个with语句中，文件对象被赋值给变量f
    f.write(requests.get(srcUrl).content)
这行代码获取了srcUrl（一个URL字符串）的内容，并将其写入到之前打开的"a.mp4"文件中
。这是通过使用Python的requests库实现的，该库用于发送HTTP请求。
具体来说，requests.get(srcUrl)向指定的URL发送GET请求。返回的是一个Response对象
，我们可以使用.content属性获取响应的原始内容（包括头信息和主体）。然后，这些内容被写入到之前打开的文件中
，使用的是write()方法。
"""
"""
https://video.pearvideo.com/mp4/short/20170512/1692250997000-10450266-hd.mp4
https://video.pearvideo.com/mp4/short/20170512/cont-1078077-10450266-hd.mp4
https://video.pearvideo.com/mp4/short/20170512/cont-t-10450266-hd.mp4
https://video.pearvideo.com/mp4/short/20170512/cont1078077-10450266-hd.mp4
"""

