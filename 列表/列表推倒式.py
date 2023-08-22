'''
需求 把字符串中的每一个字符转换成列表中的每一个元素
    1.方法一直接 一个新的列表 = list(列表的表达式的左边)
    2. 使用for in
       先定义一个空列表
       for ... in ...:
        ...点append(...)
'''
#方法1
a='haoanyou'
list1 = list(a)
print(list1)
#方法2
b = 'jianworujiantianzi'
z = []
for c in b:
    z.append(c)
print(z)
'''
列表中的for 循环 俗称列表推导式
'''
zer = 'tianzi'
zhang = [ shen for shen in zer] #这种方法可以将字符串中的字符一一列举出来
print(zhang)
renhuang = 'zhangenrui'
en = []
rui = [en for shen in renhuang]  #for 前面的是什么 就将for前面的再in都面的那个里面循环一下
print(rui)                       #for后面的那个是本身如果for前面的和后面的一样则表示将本身带入到
                                 #in右面的那个元素循环 本身可以是任意东西
""""
for循环中的循环
'''
需求1 男y 女x 将服装号 SMLX搭配一下
需求2添加到列表liebiao当中
需求3女的X型号不生产 所以不打印女的x型号  
'''
"""
#需求一
for xingbie in 'yx':
    for xinghao in 'SMLX':
        print(xingbie + xinghao)
#需求二
liebiao = []
for xingbie in 'yx':
    for xinghao in 'SMLX':
        liebiao.append(xingbie+xinghao)
print(liebiao)
#需求二第二种写法
liebiao2 = [xingbie+xinghao for xingbie in 'yx' for xinghao in 'SMLX' ]
print(liebiao2)
'''  
上面的那两个代码是相等的作用一样只不过写法不一样但是作用是一样的
第二种更简单一点写法
'''
#需求三
liebiao = []   #使用for 循环加if表达式
liebiao2 = [xingbie+xinghao for xingbie in 'yx' for xinghao in 'SMLX' if not (xingbie == 'x' and xinghao == 'X')]
print(liebiao2)
print(liebiao2)






































































