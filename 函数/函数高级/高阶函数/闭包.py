
"""
闭包
    在函数A中定义一个函数B，B函数访问A中的本地变量，并且把函数B作为返回值返回的操作
需求
    提供一个函数，用于生产一个自动增长的数字1,2,3,4,5,

结论
    1: 在函数A中定义函数B
    2: 在函数2返回函数B
    3:函数B中访问了函数A中的变量
"""
num = 0
def gat_id():
    global num #global定义一个全局变量
    num +=1
    return num
print(gat_id())
print(gat_id())
print(gat_id())
num = 0
print(gat_id())
print(gat_id())
print(gat_id())
print("="*50)
'''
使用上面的那一坨代码是可以依次递增，但是在上面运行的过程中会被打断如上面我把num从新赋值为0
它又重新开始进行递增
'''
def gat_idone():
    num1 = 0
    num1 +=1
    return num1
print(gat_idone())
print(gat_idone())
print(gat_idone())
print(gat_idone())
print("="*50)
'''
如果不通过定义全局变量在函数内进行进行赋值的话它每次调用都会进行重新赋值然后每次调用函数所得的结果是一个固定不变的值
所得的结果不是依次递增的操作
'''
def gat_idtow():
    num2 = 0
    def gen_id():
        """
        nonlocal关键字用于声明一个变量为非局部变量，即在嵌套函数中引用外部函数的变量
        使其在内部函数中可修改。当你在内部函数中需要修改外部函数的变量时，可以使用nonlocal关键字来引用该变量。
        这样，你就可以在内部函数中修改外部函数的变量，并且在外部函数中也能看到该变量的修改。
        :return
        """
        nonlocal num2
        num2 += 1
        return num2
    return gen_id
print(gat_idtow()())#因为这个是一个函数，上面的那一行返回的时候没有加括号所以调用的时候需要再后面再加一个括号
print(gat_idtow()())#上面的上面那一行后面加括号有些时候跟这个后面加括号的结果是一样的有些时候不一样
print(gat_idtow()())
print(gat_idtow()())
print("="*50)
'''
上面那一坨代码通过函数里面嵌套一个函数的方法按理来说也是可以运行的，但是每次返回的时候都还是一个恒定不变的数
只需要加一个把上面那个函数赋值给一个变量然后打印那个变量就可以完成一个递增的一个方法
下面是代码展示
'''
def gat_idthree():
    num3 = 0
    def gen_id_tow():
        nonlocal num3
        num3 += 1
        return num3
    return gen_id_tow

a = gat_idthree()
print(a())
print(a())
print(a())
num3 = 0
print(a())
print(a())
print(a())
'''
如上面的那一坨代码就可以完成依次递增的一个效果，并且不会再被从新赋值给打断了
这就是大名鼎鼎的   《闭包》
'''
print("闭包这个函数有点深奥，需要多看两边视频，视频地址就在百度网盘里面python函数也就是里面的最后一节课“闭包”")
