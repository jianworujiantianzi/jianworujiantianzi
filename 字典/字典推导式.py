xuesheng1 = {"姓名":"张同学","语文":88,"数学":99,"英语":100}
xuesheng2 = {"姓名":"李同学","语文":76,"数学":77,"英语":87}
'''
问题一
    通过循环的方式打印xueshengyi所有的信息
问题二
    找到所有的key
问题三
    把xueshenger所有的values输出出来
'''
#问题一第一种方法
a = xuesheng1.keys()
print(a)
for key in a:
    print("将key和放入这个花括号内","{}--{}".format(key,xuesheng1[key]))
#问题一第二种方法
b = xuesheng1.items()
for x in b:
    print(x)
#问题一的第三种方法
b = xuesheng1.items()
for x,y in b:
    print("{}=={}".format(x,y))   #相当与元组的拆包把元组的第一个值赋值到第一个括号里面
                                  #第二个值赋值到第二个括号里面然后循环输出
#问题一方法4
for r in xuesheng1:
    print("标记","{}--{}".format(r,xuesheng1[key]))
'''
问题二
对于字典的for遍历 默认遍历所有的key
'''
for tianzi in xuesheng1:
    print(tianzi)
#问题三
c = xuesheng2.values()
for cc in c:
    print(cc)
'''
需求 生成1-10 之间所有数的平方 并且对应起来
'''
f = {renyishu:renyishu**2 for renyishu in range(10)}
print(f)














































