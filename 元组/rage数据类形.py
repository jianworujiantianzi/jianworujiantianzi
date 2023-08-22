'''
1.创建方法
    创建一个[0,10)的整数数据  rage是一个有序序列
'''
#1.
a = range(10)
print(a)
print(len(a))
for x in a:
    print(x)
print(type(a))
list1 = list(a)
print(list1)
print("="*50)


#从1数到100步长为2  也就是被二整除的全部都不打印
for o in range(1,100,2):
    print(o)























