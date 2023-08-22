'''
函数function
    分类
        1.无参数，无返回值
        2.无参数，有返回值
        3.有参数，无返回值
        4.有参数，有返回值
'''
#1.无参，无返
def taok():
    print("好好学习天天向上")

taok()

#2.无参，有返
def a():
    return "123456789"
a1 = a()
print(a1)

#3.有参，无返
def b(c):
    print("插入数据{}成功".format(c))
b(123)

#4.有参，有返
def c(x,y):
    print(x,y)
    return x+y
c1 = c(1,2)
print('结果:',c1)










