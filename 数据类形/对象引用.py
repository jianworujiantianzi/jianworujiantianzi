'''
浅拷贝
第一种拷贝方法   拷贝的时内存地址值 无论变哪一个全部都会发生改变
'''
import copy

a = [1,2,3,4]
b = a
b[0] = 100
print(a)
print(b)

'''
深拷贝
第二种拷贝方法  直接创建一个新的对象出来把新对象的内存地址值赋给一个新值 
这样子改变新值里面的东西原来值里面的东西就不会发生改变
'''
a2 = [7,8,9,10]
b2 = a2[:]
b2[0] = 100
print(a2)
print(b2)
'''
比深拷贝还要深的拷贝方法 , 导入拷贝 导入拷贝有两种拷贝方法一种是用python中的copy库中的copy另一种方法是
用copy库中的deepcopy这种拷贝方法是更深一层的拷贝方法
'''
#1. 用copy点copy  浅拷贝也叫做分片拷贝
d = [0,[1]]
e = copy.copy(d)
e[0] = 50
print(d)  #d的第一个值没有改变
print(e)
e[1][0] = 50
print(d)  #d[[]]里面的值发生了改变  所以这个是浅拷贝
print(e)
#2.用copy.deepcopy
f = [1,[2]]
g = copy.deepcopy(f)
g[0] = 80
print(f)    #没有发生改变
print(g)
g[1][0] = 60
print(f)    #两个被拷贝的值都没有发生改变所以是深拷贝
print(g)






















