'''
reduce
需求list_a=[2,4,6,8,10] 算出2*4*6*10总之把他们里面的所有元素进行相乘成绩的一个和
reduce通常进行累计运算比如说加法乘法减法之类的运算
        注意:
            reduce是python中的一个内置模块要先进行导入才能进行使用导入方法如下
            from functools import reduce

'''
from functools import reduce
list_a=[2,4,6,8,10]
ret = 1
for x in list_a:
    ret *= x
print(ret)
print("1"*50)
"""使用reduce方法进行上面的操作"""
list_b = [2,4,6,8,10]
aaaa=reduce(lambda x,y: x*y,list_b)
print(aaaa)
'''
上面的那一坨代码详细解释
    运行第一次的时候把列表当中的第一个值赋值给x第二个值赋给y然后进行运算返回值
    :return 2*4 = 8
    然后第二次循环把上一次return (这个单词就是返回值的意思)返回的值8赋值给x列表中的第三个数6赋值给y
    ：return 8*6 = 48
    第三次循环是把上一次return返回的48赋值给x列表中的第四个数值8赋值给然后进行运算
    :return 48*8 = 384
    第四次循环是把上一次return返回的384赋值给x然后把列表中的最后一个值10赋值给y进行运算
    :return 384*10 = 3840
'''