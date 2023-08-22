"""
a=1
while a<=5:
    a+=1
    b = 1
    while b <=a:
        print('*',end='')
        b += 1
    print()

'''
这里面的%号是占位符号，没有作用，但不能没有，不然的话会报错。
'''
#原理代码展示
#第一行
hang = 1
print("1*1=%a"%(1*hang),end=' ')
print()
#第二行
hang += 1
print("1*2=%a"%(1*hang),end=' ')
print("2*2=%a"%(2*hang),end=' ')
print()
#第三行
hang += 1
gao = 1
'''
"%d*%d=%d"这个是占位符后面应再跟一个占位符%，占位符后面的(gao,hang,gao*hang)刚好按顺序对应前面的值
%后面跟不同的字母会有不同的站位效果：
列如
d：整数占位符，用于表示整数类型的值。
f：浮点数占位符，用于表示浮点数类型的值。
F：浮点数占位符，用于表示浮点数类型的值，与 f 相同。
e：科学计数法占位符，用于表示浮点数类型的值，以科学计数法的形式显示。
E：科学计数法占位符，用于表示浮点数类型的值，以科学计数法的形式显示，与 e 相同。
g：实数占位符，用于表示浮点数类型的值，根据数值的大小选择 f 或 e 的显示方式。
G：实数占位符，用于表示浮点数类型的值，根据数值的大小选择 f 或 E 的显示方式，与 g 相同。
r：字符串占位符，用于表示字符串类型的值，将字符串转换为它的原始形式（raw string）。
s：字符串占位符，用于表示字符串类型的值，将字符串转换为它的原始形式（raw string），与 r 相同。
'''
print("%d*%d=%d"%(gao,hang,gao*hang),end=' ')
gao+=1
print("%d*%d=%a"%(gao,hang,2*hang),end=' ')
gao+=1
print("%d*%d=%a"%(gao,hang,3*hang),end=' ')
"""
hang = 1
while hang <= 8:
    gao = 1
    while gao <= hang:
        print("%d*%d=%a"%(gao,hang,gao*hang),end=' ')
        gao += 1
    print()
    hang += 1
