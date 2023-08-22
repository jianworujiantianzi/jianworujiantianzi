"""
re模块是python里面的内置模块
"""
import re
"""
findall(谐音：饭兜)  然后里里面给的第一个参数是正则表达式
第二个参数放的是源字符串是什么
"""
a = re.findall("z","我的偶像是zjl,zhoujielun")
print(a)
"""
因为\再python中是转义字符的意思所以要在前面价个r来取消转义
"""
aa = re.findall(r"\d+","我今年18岁,我有200000快")
print(aa)
"""
finditer(谐音:饭的一他)  
下面的那一行直接打印的是一个迭代器
"""
print("="*50)
a1 = re.finditer(r"\d+","朕的江山5000年,朕能活8000岁")
"""
通过循环再迭代器上面拿到内容
    返回的数据<re.Match object; 被匹配的一个选项
    span=(第几个数字到第几个数字)
    match=返回的一个结果
如果只想要数据可以再后面加一个
    .group()
    
"""
#这个是重点要多多练习
for ss in a1:
    #print(ss)
    print(ss.group())#从匹配到的结果拿到数据

print("="*50)

"""
re，search   这个只会获得到第一个匹配的内容
但是后面的内容不会匹配到  
"""
asa=re.search(r"\d+","我叫周杰伦,今年32岁,我的班级是5年4班")
print(asa.group())  #用.group拿到纯数据
print("="*50)
"""
match
match再匹配的时候，是从字符串的开头进行匹配的，类似与再正则前面加上了一个^
search 和 match的区别就是 search再里面搜第一个 match从开头开始搜
"""
asb=re.match(r"\d+","我叫周杰伦,今年32岁,我的班级是5年4班")
print(asb)
print("="*50)
"""
预加载，提前把正则对象加载完毕 
.compile(谐音:康派哦:预加载的意思)
"""
jiazai = re.compile(r"\d+")
#直接把加载好的正则进行使用  想用那个就直接调用就好了
qq = jiazai.findall("我叫周杰伦,今年32岁,我的班级是5年4班")
print(qq)
