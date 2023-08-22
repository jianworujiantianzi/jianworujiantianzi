'''
高阶函数
    所谓高阶函数，需要满足下面的两个条件之一
        1.接收一个或者多个函数作为参数
        2.输出一个函数
'''
'''下面这一坨代码就称之为高阶函数因为他传进去的参数是一个函数所以就被称为高阶函数'''
def fun_a(callback):#定义一个函数函数传进去的是一个函数类形
    """
    :callback: function
    :return:
    """
    callback()#调用函数
    return 1
def fun_b():#定义第二个函数
    print("fun_b") #打印一个任意的东西
fun_a(fun_b)#调用第一个函数里面传入第二个函数第二个函数后面不能再加括号
print("*"*40)
def fun_c():
    print("fun_c")
    return fun_b  #返回的是一个函数所以这个也是一个高阶函数
sss=fun_c()
print(sss)
print("-"*50)
fun_c()#直接调用返回print
sss()#赋值调用返回return
print("^"*50)
"""内置的一些高阶函数的用法"""
"""
map()
    map是一个映射，接收两个参数第一个参数是函数，第二个参数是一个可迭代的对象如/序列(列表/元组/集合等等)
        返回值也是可迭代的对象list(ret)转换为序列
需求一
    有一个列表[1,2,3,4,5]给每一个  元素都加上10,并且生成一个新的列表
  
"""
#需求一
list_a = [11,12,13,14,15]
list_b = []
#思考一个问题:对于list_b中的一个数据，是由list_a中的数据根基一个新规则得出
#也就是说list_a和list_b之间是由一一对应的关系就像健值对一样
#既然是一一对应的那么就可以使用 map映射去做相同的事情
for a in list_a:
    list_b.append(a+10)
print("list_b",list_b)
print("%"*50)
fn = lambda x:x+10 #因为map里面要传一个函数所以定义一个函数
ret=map(fn,list_a) #map里面需要放一个函数和一个序列
print("list_b",ret)#返回值是一个可迭代对象可以使用list()转换为列表
print(list(ret))
print("x"*50)
'''
需求
    lista[11.12,13,14,15,16,17,18,19]
    listb[21,22,23,34,25,26,27,28,29]
    把这两个列表里面的值进行相加

'''
lista=[11.12,13,14,15,16,17,18,19]

listb=[21,22,23,34,25,26,27,28,29]
''' 
lambada后面的x,y表示放入两个参数x,y  x+y加上这个之后就是一个处理函数
然后这个lambada后面的x是遍历lista中的所有数据，后面的y是遍历listb中的所有数据
'''
aaa=map(lambda x,y:x+y,lista,listb)#有几个列表对象就需要写多少个参数进去这里面就两个所以就写了两个参数进去
print(list(aaa))#返回可迭代对象需要加一个list才能将其返回



























