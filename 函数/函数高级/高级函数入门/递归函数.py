"""
递归函数
    所谓递归函数A执行到某一个时机的时候，自动的调用函数自己的以中操作方式，应为会
涉及到自己调用自己的一种情况，所以需要避免死循环的出现,因此递归函数一定要有出口
"""
'''需求，定义一个函数用来求某一个数以内所有整数和'''
def qiuhe(x):
    """
    用于计算x以的所有整数和
    x :int类形
    :return:0--x之间的所有整数和
    """
    value = 0
    for a in range(1,x+1): #当 a 的值大于 x 时，循环条件不在满足自动退出循环
        value+=a
    return value
print(qiuhe(100))
print("*"*80)
'''
上面的那一坨代码的原理
qiuhe(1)=1                  qiuhe(1)=1
qiuhe(2)=1+2                qiuhe(2)=2+qiuhe(1)
qiuhe(3)=1+2+3              qiuhe(3)=3+qiuhe(2)
qiuhe(4)=1+2+3+4            qiuhe(4)=4+qiuhe(3)
                            规律每一个数的累计和等于当前数加前一个数的累计和
                            qiuhe(100)=100+qiuhe(99)
                            qiuhe(x)=x+qiuhe(x-1)
                            ......
所以根据这一个原理可以得出一个简化的代码如下面的那一坨
        注意一定要写出口不然会报错也就是不会调用自己的地方
        在这托代码当中出口就是else
'''
def qiuhe2(x):
    value = 0  #value的初始值为0
    if x >1:  #如果x大于1则执行类似于qiuhe(x)=x+qiuhe(x-1)
        value = x + qiuhe2(x - 1) #这坨代码运行的时候会自己调用自己
    else:  #如果不满足就将qiuhe的值为1进行返回
        value = 1 #其实这个可以写成vale =1+qiuhe2(0)但是没有必要直接写成这个等于1就行
    return value
print(qiuhe2(100))
