'''
当函数被调用时，在函数完成工作后，
需要将控制权返回给使用者，函数是通过return语句将结果传递给使用者，并接受当前函数的运行
如果明确的使用teyurn进行了返回，那么函数返回值是teturn后面的值
如果没有使用teturn进行返回那么函数返回值是None
可以返回多个值，会使用一个元组进行封装
'''
def fn():
    print("执行参数一")
#定义一个fn的返回值
f1 = fn()
print("返回参数一",f1)   #没有使用teyurn所以返回的是None

def fs():
    print("执行参数二")
    return 100,200,300  #如果是多个值默认把return后面的元素装包到一个元组里面
f2 = fs()
print("返回参数二",f2)    #使用了return所以返回的是return后面的值
print(type(fn()))
