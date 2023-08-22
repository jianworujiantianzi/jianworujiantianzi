""""""
"""
第一步:先安装模块
第二部 导入模块
"""
from bs4 import BeautifulSoup
html ="""
      <ul>
          <li><a href="zhangwuji.com">张无忌</a></li>
          <li id="abc" ><a href="zhouxingchi.com">周星驰></a></li>
          <li><a href="zhubajie.com">猪八戒</a></li>
          <li><a href="wuzetian.com">武则天</a></li>
          <a href="jinmaoshiwang.com">金毛狮王</a>#应为这个a标签不再li标签里面所以这个就拿不到
                                                        直接被过滤掉
      </ul>
"""
#初始化BeautifulSoup对象
page = BeautifulSoup(html,"html.parser")
"""
点find(谐音;范的)
page.find("标签名",attrs={"属性":"值"})   #查找某个元素,只会找到一个结果
当然还可以接着往下找 就是往里面套娃  就比如说再下面的结果里面再接着找a标签     代码展示如下
"""
li = page.find("li",attrs={"id":"abc"})
print(li)
a = li.find("a")
print(a)
"""如果只想拿里面文本可以再结尾加一个.text这个就是文本的意思"""
print("文本:",a.text)
"""如果只想要里面属性的值可以.gat("属性值") 因为href(谐音:孩夫)后面跟的一般都是属性值所以如下操作即可"""
print("属性值",a.get("href"))
print("="*50)
"""
.find_all
.find_all和上面的.find的区别就是查找一个find_all是找全部     #找到一堆结果
一般这个要和.find搭配上循环使用不然直接把所有的东西都弄过来看着有点乱   #示列如下
"""
b = page.find_all("li")
print(b)        #这样子看着里面很乱  如果想要li里面的a标签里面的内容不好找那就要用上循环了
print("="*50)
for li1 in b:
    ax=li1.find("a")
    tixt = ax.text
    zhi = ax.get("href")#这里面的a是a标签的意思    放在全部里面就是li标签当中的a标签
    print(tixt,zhi)