import requests
from bs4 import BeautifulSoup
"""第二十步的分步"""
n = 1   #图片名称
"""第一步导入网址"""
url = "https://www.umei.cc/bizhitupian/xiaoqingxinbizhi/"
"""第十步写父站的网址    注意绝对路径和相对路径"""
p = "https://www.umei.cc"
"""第二部请求"""
resp = requests.get(url)
"""第三是步解码"""
resp.encoding="utf-8"
"""第四步检查是否能够把代码打印出来"""
# print(resp.text)
"""第五步进行初始化"""
main_page = BeautifulSoup(resp.text,"html.parser")
"""第六步再网址里里面找到所有带有class=img_album_btn属性的a标签"""
abiaoqian = main_page.find_all("a",attrs={"class":"img_album_btn"})
"""第七步先看一眼长度有没有问题如果能够打印出来长度就是没有问题"""
# print(len(abiaoqian))
"""第八步设置一个循环把上一步找到的所有的a标签中的href的值给打印出来利用gat把里面所有有href的值全部都请求出来"""
for a in abiaoqian:
    href = a.get("href")
    """第九步把请求出来的东西打印出来  
    注意
    如果打印出来的第一个字符不是/这时就要找到父网站里面的最后一个杠
    然后把父网站最后一个杠后面的东西去掉然后再拼接"""
    print(href)
    """第十一步打印出来的都是一些子集也就是子网站需要个父网站进行拼接才能使用"""
    zong=p+href
    """第十二部打印拼接好的网站"""
    print(zong)
    """第十三部访问拼接好的网站"""
    whang_zhan = requests.get(zong)#请求到子页面
    """第十五步 检测到十四步骤打印出来的代码有乱码的出现所以进行一个解码"""
    whang_zhan.encoding = "utf-8"
    """第十四步查看子页面访问的有没有问题    因为是测试所以不用全部都的打印出来 后面加一个break就可终止循环"""
    # print(whang_zhan.text)
    # break
    """第十六步 找到img标签 因为这个标签是在前端里面存放图片的一个标签
    一般这个标签太难找到正确的所以要找他爹的的标签 看看特爹的属性的属性有什么 一般找他爹的class"""

    """第十七步对子网站进行初始化"""
    whang_bs = BeautifulSoup(whang_zhan.text,"html.parser")
    """第十八步找到图图片存放的img标签的父标签 为了精确查找要把父标签的属性加上"""
    div = whang_bs.find("div",attrs={"class":"big-pic"})
    """第十九步，因为要找的不是父标签找的是父标签里面的img标签，所以再从副标签里面找img
    因为img标签里面存的是下载路径所以主要目的是找下载地址"""
    src=div.find("img").get("src")#找到img标签并把且要去拿里面的src的下载路径
    """第二十步，查看图片地址能否打印出来"""
    # print(src)
    # 下载图片
    """第二十一步，下载图片操作"""
    """首先发送一个网络请求到这个图片的下载地址"""
    xia = requests.get(src)
    """
    思考
    因为这个是一个图片所以想要这个图片的文本打印不了所以不能用print(xia.test)
    .text是文本的意思打印这张图片的文本没有什么用获取不了不说拿它也没有用
    要xia.content这样子去那content是响应体的字节发的形式 图片不能变成字符窜
    等于说 把这些字节存起来就好了存储方式如下
    """
    """
    这个代码的意思是
    with open
        这是一个简单的一个with语句意思是打开的意思
    f"{n}.jpg" 文件的变量名为n加上".jpg"，也就是说文件的名字叫做n.jpg 因为是图片所以要加上jpg
    mode="wb"的意思是以二进制模式写入文件
    f.write(xia.content)
    使用write方法把图片地址写入文件因为后面是.content所以是以字节的形式写如
    注意:
        写入文件的是字节所以必须要写wb    w就不行了w是写文本的
    """
    # print(xia)
    # with open(f"{n}.jpg", mode="wb") as f:
    #     f.write(xia.content)
    #     """
    #     这句话中；两个f的用法
    #     第一个"f"是作为with open语句的一部分，用于打开文件并返回文件对象。在这个上下文中
    #     ，"f"是一个文件对象，代表打开的文件。通过使用with语句，Python会自动处理文件的关闭操作
    #     ，确保在代码块执行完毕后文件被正确关闭。
    #     """
    #     print(f"第{n}张图片下载完毕")
    #     n += 1









