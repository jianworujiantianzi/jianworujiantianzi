'''
列表和字典的区别
对于列表来说是一个有序可变的集合,我们可以通过对应的索引去获取列表中每一个元素，但是如果使用字典的话，其中的
数据是一个无序的可变集合,我们不能通过索引获取对应的元素，我们使用的是 健 值 对
字典的他点
1.每一个字典都有一个健和值对应       键(key)    值(vale
2.通过健获取对应的值
3.字典当中不能存可变类形的数据
'''
#创建一个空字典
a = {}
#创建一个简单查询的字典
b = {'z':'张恩瑞','zer':'天子'}
print(b['z'])
'''
字典添加字段     如下
'''
#给张三添加一个总成绩
'''
注意再这个表达式里面只能用上引号进行算数不然会报错原理还不是很清楚反正结论就是不能用单引号不然会报错
'''
zhangsan = {"姓名":"张三","语文":80,"数学":96,"英语":90}
zhangsan["总成绩"] = zhangsan["语文"] +zhangsan["数学"] + zhangsan["英语"]
print(zhangsan)
'''
修改  第一个方法张三的英语成绩为100分    操作如下        下面还有另外的方法
重点  有字段则修改  没字段则添加
'''
zhangsan["英语"] = 100
print(zhangsan)    #这个总成绩没有改变是应为没有加入计算
zhangsan["总成绩"] = zhangsan["语文"] +zhangsan["数学"] + zhangsan["英语"]
print(zhangsan)

'''
删除 
    1.使用del 列如把语文成绩删除掉 操作如下
    2.使用.pop("输入要删除的键")  如果删除没有的会直接报错
'''
del zhangsan["语文"]
print(zhangsan)

'''
通过方法 第一个参数 键 第二个参数，如果没有对应的健,返回第二个参数的值
'''
print("获取成绩英语",zhangsan.get("英语"))
print("获取成绩物理",zhangsan.get("物理"))  #没有则返回None
print("获取成绩化学",zhangsan.get("化学",100)) #如果字典里面没有就可以像这样
                                            #再后面直接添加想获取的值
'''
修改的第二种方法
    使用.update([()])把姓名改成王五   操作如下
'''
zhangsan.update([("姓名","王五")])
print(zhangsan)
'''
存    把张同学和李同学的成绩存到一个集合当中
'''
xuesheng1 = {"姓名":"张同学","语文":88,"数学":99,"英语":100}
xuesheng2 = {"姓名":"李同学","语文":76,"数学":77,"英语":87}
list1 = [xuesheng1,xuesheng2]
print(list1)
#如果觉得不好看可以用for循环换行    操作如下
for m in list1:
    print(m)
'''
可以通过 in 来查询一个数据是否存在一个字典当中 
    如果存在则返回 True  如果不存在则返回Fals
注意
    in再字典当中是用来判断key是否存在
'''
#查询李华是否在xueshengyi当中
print("李华" in xuesheng1)

'''
获取所有的key方法 
    使用keys()方法       举列获取xueshengyi当中所有的key
'''
print(xuesheng1.keys())  #获取xueshengyi当中的所有key
'''
获取所有的value方法
    使用values方法        举例获取xueshengyi当中所有的values
'''
print(xuesheng1.values())
'''
获取全部的健值对
    使用.items
    输出的是一个个的元组 应为健值对就是通过一个个的元组来表示的
'''
print(xuesheng1.items())





















