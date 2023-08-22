from lxml import etree
xml = """
<book>  
    <id></id>  
    <name>遍地野花香</name>  
    <name>遍地野花香1</name>  
    <price>1.23</price>  
    <nick>臭豆腐</nick>  
    <author>  
        <nick id="10086">周大强</nick>  
        <nick id="10010">周芷若</nick>  
        <nick class="jay">周杰伦</nick>  
        <nick class-="">蔡依林</nick>  
        <div>  
            <nick>惹了</nick>  
        </div>  
    </author>  
    <partner>  
        <nick id="ppc">胖胖胖</nick>  
        <nick id="ppdb">胖胖不胖</nick>  
    </partner>  
</book> 
"""
#此时做练习只能用XML了
et = etree.XML(xml)
"""
使用xpath解析因为从上面的那些代码要从根节点开始找、
根节点去找的时候用/就可以去找了”/“代表的是跟再此代码中找的是book
所以就如下放方式去找根节点
"""
result = et.xpath("/book")
"""先打印一下看看打印出来的结果如果是Element就代表是找到了并且后面跟的就是这个节点"""
print(result)
"""但是我们要找的是儿子的内容怎么找呢    请看下面
xpath中间那个杠代表儿子 """
result_zi = et.xpath("/book/name")
print(result_zi)
"""我们要找的是里面的文本想要那文本的话就需要再下面加上一个操作"""
result_zi_wen = et.xpath("/book/name/text()")   #text()拿文本
print(result_zi_wen)
"""这时候拿到的是一个列表 要是只想要里边的字的话只需要后面加一个列表就可 
想要拿到第几个数据就再列表中协商要拿到的那个数据的位置在列表中即可"""
result_zi_wen = et.xpath("/book/name/text()")[1]
print(result_zi_wen)
print("="*50)
"""
需求1.
    找到xml里面的所有nike标签
解决办法如下用；两个杠来表示的是子孙后代 所有的如下方法就可以把所有的子集给找出来
如果想要把文本打印出来只需要再后面加一个/nack就是要里面的文本的意思
"""
z = et.xpath("/book//nick/text()")
print(z)
print("*"*50)
"""
需求二
要所有的book的孙子辈的nick
头疼的一些地方
因为这里面的nick的父辈都不一样要是一个一个的找的时候可能太麻烦了
所以我们这时候就需要一个爱谁谁*这个爱谁谁的使用方法如下
只需要再//中间加一个*就代表任意的了 大白话来说就是儿子节点谁都行的后代  也就是孙子辈分的人
"""
z1 = et.xpath("/book/*/nick/text()")#   *通配符.谁都行
print(z1)
"""
难度升级
再这么多的nick标签里面找到周杰伦
分析
    首先我们要找到这个周杰伦的位置我们这样et.xpath("/book/author/nick/text()")可以找到author中的
    所有的nick标签想要再具体到周杰伦就要用下面的方法就是添加属性
"""
#添加属性
"""
属性的添加
    我们再需要找的属性的对应的标签然后再对应的标签后面加上属性   具体的添加方法如下
    在后面加一个中括号里面加上@后面跟上一个属性
这里面的中括号表示的是属性的筛选    @是属性名 = 值
"""
zjl = et.xpath("/book/author/nick[@class='jay']/text()")[0]
print(zjl)

"""
需求3拿到partner里面的id的值
    方法如下
    下面这句话的最后两个nake/@id  表示的是nake里面的id属性
    @是属性可以直接拿到属性值   因为拿到的不是里面的文字所以不用text
"""
idz = et.xpath("/book/partner/nick/@id")#最后一个杠表示拿到nake里面的id的值
print(idz)