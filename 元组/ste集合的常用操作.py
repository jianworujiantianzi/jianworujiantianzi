'''
集合添加元素
    使用.add  只能够添加一个不可变的数据
    可以添加像元组这种不可变的数据 不能添加列表这种可变的数据
集合删除元素
    指定删除  使用.remove 删除指定的元素
    随机删除 使用.pop
    清空删除 使用.clear


'''
#操作   添加6
s1 = {0,1,2,3,4,5}
print(s1)
s1.add(6)
print(s1)
#操作   删除2
s1.remove(2)
print(s1)
#操作   随机删除
w = {'a','b','c','d'}
w.pop()
print(w)
#操作   清空数据
b = {1,2,3,4,5,6,7,8,9,0}
b.clear()
print(b)
'''
集合和集合之间的运算
    1.交集运算
    通过使用 & 符号来将集合的交集来算出来
    2.并集运算
    通过使用 | 符号来将集合的并集来算出来
    3.求差集
    直接用减号即可完成计算
'''
#计算两个集合的交集
jiheyi = {1,2,3,4,5,6}
jiheer = {4,5,6,7,8,9,}
print(jiheyi & jiheer)    #通过使用 & 符号来将集合的交集来算出来

#计算两个集合的并集
print(jiheyi | jiheer)    #   通过使用 | 符号来将集合的并集来算出来
#计算两个集合的差集
print(jiheer - jiheyi)    #通过使用 - 号来将集合的差集来算出来
'''
1.集合便利
    使用for循环历捷集合
2.集合推导式    2.
'''
#集合便列
zer = {'见','我','如','见','天','子'}
for shen in zer:
    print(shen)
#集合推导式
renhuang = {nvdi for nvdi in range(10)}
print(renhuang)
#加一个if语句就可以把语速调节 如下就是把语速每隔二个全部不输出
renhuang = {nvdi for nvdi in range(10) if nvdi%2}
print(renhuang)































