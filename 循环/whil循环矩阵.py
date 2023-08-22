'''
end=""#空字符串  则表示不换行的意思 引号里面可以放东西比如空格，放一个空格的话则输出结果之间会空一格
print 在这里指的是换行的意思
退出当前循环continue  退出当前循环执行下一次循环
退出循环 break    终止全部循环
'''
#第一行
print("*",end="")
print("*",end="")
print("*",end="")
print("*",end="")
print("*",end="")
#换行
print()
#第二行
print("*",end="")
print("*",end="")
print("*",end="")
print("*",end="")
print("*",end="")
#换行
print()
#第三行
print("*",end="")
print("*",end="")
print("*",end="")
print("*",end="")
print("*",end="")
print()
'''
加上whil循环之后 第一代升级
'''
xunhuan = 1
while xunhuan <=5:
    print("*1",end="")
    xunhuan += 1
xunhuan = 1
print()
#第二行
xunhuan = 1
while xunhuan <=5:
    print("*1",end="")
    xunhuan += 1
xunhuan = 1
print()
#第三行
xunhuan = 1
while xunhuan <=5:
    print("*1",end="")
    xunhuan += 1
xunhuan = 1
print()

'''
使用whill循环中嵌套whill循环，  实现第三代升级
'''
a1=1
while a1 <=5:
    while xunhuan <=5:
        print("*2",end="")
        xunhuan += 1
    xunhuan = 1
    print()
    a1+=1






'''
a=0
while a<=5:
    print('*************')
    a+=1
'''