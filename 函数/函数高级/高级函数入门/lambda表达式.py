"""
lambada表达式
    在python中除了def可以声明一个函数以外,使用lambada表达式也是生成函数对象的表达形式,
对于一个比较简单，在函数体只有一小部分代码的时候，使用lambada表达式的时候更加清晰。
    语法格式:
    fn = lambada[参数,参数一,参数二,3,]执行语句
    在lambada表达式中可以有多个执行语句多个执行语句用分号隔开，如果有返回值放到
        lambada表达式一般都是写一些比较简单的一些表达式复杂一点的函数还是要用def来定义
"""
def sun(x,y):
    """求和计算"""
    return x+y
#和上面的一样，但是更加清新
sun2 = lambda x,y:x+y  #通过lambada表达式简化代码 lambada可以是一个所谓的函数参数
print(sun(1,2))
print(sun2(5,6))
print(sun2)
"""如上面这串代码显示，这个sun2也是一个函数名使用lambada定义的"""
def go(huidiao):
    print("开始执行")
    huidiao()
    print("完成执行")
go(lambda :print("lambada函数")) #这样写可以省略一个参数
print("="*50)
#def v(x1,y1):
"""返回x1y1中的最大值"""
"""
    if x1>=y1:
        return x1
    else:
        return y1
"""
    #三元运算符 如果是则返回第一个参数if前面的如果不是则返回第二个参数elass后面的
    #return print("第一个参数") if x1 >= y1 else print("第二个参数")
xxx = lambda x1,y1:print("第一个参数") if x1 >= y1 else print("第二个参数")
print(xxx(50,12222))
'''print(v(50,1000))'''
print("="*50)
'''三元运算符'''
def sanyuanyunsuan(xa,ya,za):
    """返回xa,ya,za的最大值"""
    if xa>=ya and xa>=za:
        return xa
    elif ya>=xa and ya>=za:
        return ya
    elif za>=xa and za>ya:
        return za
print(sanyuanyunsuan(50,810,88))
print("="*50)
'''和上面那个是一样的功能'''
def sa(xa,ya,za):
    """返回xa,ya,za的最大值"""
    if xa>=ya and xa>=za:
        print(xa)
    elif ya>=xa and ya>=za:
        print(ya)
    elif za>=xa and za>ya:
        print(za)
sa(20,50,80)
print("="*100)
'''还是上面的上面的那一坨代码的另一种书写形式'''
def tiaozheng(x,y,z):
    return x if x>=y and x>=z else y if y >=x and y>=z else z
print(tiaozheng(50,88,65))
'''上面的上面的的上面那一坨代码使用lambda函数书写'''
print("="*100)
tiaozhenger = lambda x,y,z:x if x>=y and x>=z else y if y >=x and y>=z else z
print(tiaozhenger(50,80,9))
print("使用labada函数的时候太长的话不建议使用应为不够清晰看着跟一坨答辩一样"
      "没有def函数写的那样清晰如果代码比较短的时候使用lambda长的话还是用def")
print("-"*50)
'''在表达式中执行多个语句'''
"""在表达式中执行多个语句需要使用逻辑运算符or 或者 and"""
'''这样就可以把多个print放到同一行了'''
luoji = lambda a,b,c:print(a)or print(b)or print(c)
luoji(2,3,4)

































