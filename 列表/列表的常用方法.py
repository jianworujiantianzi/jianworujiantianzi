'''
增加
    1.再末尾添加 使用.apend方法在原来基础上进行修改
        和切片不一样的是切片是先删除在修改，而这个是直接修改
    2.插入方法 （索引）使用.inster(索引)方法找到索引进行插入
删除
    1.根据值来删除 使用.remove
查询
    1. count(谐音：康特 )用于查找值 如果存在则返回1 不存在则返回0
    2.index(谐音：阴怼可思)用于查找索引 如果存在则返回索引值,如果没有则报错
    3.in
合并
    1.如果想要把列表合并起来可以用.extend来合并 相当与在后面插入一个列表并合并
倒叙
    1.通过reverse可以把列表中的元素给倒叙一遍
'''
lista=['a','b','c','d']
print(lista)
lista.append('e')#在末尾添加一个元素e
print(lista)
lista.insert(3,3)#再第三个索引后面插入一个3
print(lista)
listb=['A','B','C']
listb.remove('C')#直接把要删除的东西输入进来就删除了
print(listb)
print('count a',lista.count('d'))#存在返回1，不存在返回0
print(listb.index('B'))#索引是几就返回几,如果没有报错
print('A' in listb)
listb.reverse()
print(listb)
'''
使用append()方法可以向列表末尾添加一个元素，例如：

python
my_list = [1, 2, 3]  
my_list.append(4)  
print(my_list) # [1, 2, 3, 4]
使用insert()方法可以在指定位置插入一个元素，例如：

python
my_list = [1, 2, 3]  
my_list.insert(1, 4)  
print(my_list) # [1, 4, 2, 3]
删除元素：
使用remove()方法可以删除指定元素，例如：

python
my_list = [1, 2, 3]  
my_list.remove(2)  
print(my_list) # [1, 3]
使用pop()方法可以删除并返回指定位置的元素，例如：

python
my_list = [1, 2, 3]  
my_list.pop(1)  
print(my_list) # [1, 3]
替换元素：
使用replace()方法可以替换指定位置的元素，例如：

python
my_list = [1, 2, 3]  
my_list[1] = 4  
print(my_list) # [1, 4, 3]
获取元素：
使用索引可以获取指定位置的元素，例如：

python
my_list = [1, 2, 3]  
print(my_list[1]) # 输出2
切片操作：
可以使用切片操作获取列表的一部分，例如：

python
my_list = [1, 2, 3]  
print(my_list[1:]) # [2, 3]
列表长度：
使用len()函数可以获取列表的长度，例如：

python
my_list = [1, 2, 3]  
print(len(my_list)) # 输出3
循环遍历：
可以使用for循环遍历列表中的每个元素，例如：

python
my_list = [1, 2, 3]  
for item in my_list:  
    print(item)
    '''
