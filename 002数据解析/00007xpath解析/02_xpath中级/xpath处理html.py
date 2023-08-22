from lxml import etree
htmla = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <ul>
        <li><a href="http://www.baidu.com">百度</a></li>
        <li><a href="http://www.google.com">谷歌</a></li>
        <li><a href="http://www.sougou.com">搜狗</a></li>
    </ul>
    <ol>
        <li><a href="feiji">飞机</a></li>
        <li><a href="bapao">大炮</a></li>
        <li><a href="huoche">火车</a></li>
    </ol>
    <div class="job">李嘉诚</div>
    <div class="common">胡辣汤</div>
</body>
</html>

"""
et = etree.HTML(htmla)
"""
需求一：
    只要ul里面的第二个li标签
解决方案：
    再li标签里面加上一个列表后面跟上要拿的第几个
实战案列如下
"""
li_list = et.xpath("/html/body/ul/li[2]")
print(li_list)
"""
需求二：
    把需求一里面的文本提取出来
思考:
    看一下文本再的一个位置然后这里面的文本被a标签包裹这的所以在后面加上一个a标签因为是文本所以后面要加上一个text()
实战案例如下 
"""
li_list_a = et.xpath("/html/body/ul/li[2]/a/text()")
print(li_list_a)
"""
需求三:
    拿到页面里面li标签 并且希望拿到里面的url和里面的名称
思考;
    我们发现这里面的所有的li标签里面都包含这a标签然后url都再a标签里面的属性值上面名称都再a标签包裹这
    我们想拿到的话刚好//表示的是所有的意思所以我们刚好利用//的特性把所有的li找出来再根据循环进一步提取
    然后./表示的是当前的节点再循环里面利用./的特性再接着找
"""
quan_li = et.xpath("//li")
for li in quan_li:
    """
    这个./表示的是当前节点 然后这里面的当前节点就是li也就是说再上面的一堆li标签一个一个的找的意思
    后面跟上一个@href也就是说属性href对应的值
    """
    url_a = li.xpath("./a/@href")
    """
    因为还要拿到文本所以后面再加上一个text()
    """
    wen_ben= li.xpath("./a/text()")
    #最后打印一下就ok了
    print(url_a,wen_ben)

    """
    注意打印的时候最好像这样一对一对的去打印
    因为后续的爬虫工作......
    """
