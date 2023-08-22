'''
需求
    给定一个list集合，把其中所有数据大于80的数据全部找出来
'''
#传统方法一
lis = range(100)
for x in lis:
    if x >= 80:
        print(x)
#传统方法二
lista = range(100)
lista1 = []
for xx in lista:
    if xx >80:
        lista1.append(xx)
print(lista1)
print("*"*100)
"""
使用filter(这个位置写函数,这个位置写序列)函数 用来过滤
这里面写函数的地方接收一个参数返回一个布尔值
    使用方法如下
"""
listsss=range(100)
nnn = filter(lambda x:x>80,listsss)
print(list(nnn))
'''
上面的那个代码的运行原理
    先用filter遍历listsss里面的每一个元素，然后进行判断，判断结果如果是正确的就返回True,返回True就可以通过list把
里面的数据给提取出来
    如果不是正确的就返回False 然后就不返回数据了，等于这个数据就直接过滤掉了 
'''