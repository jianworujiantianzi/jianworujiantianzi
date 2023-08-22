'''
参数的解包
在元组前面加一个*就可以进行元组的拆包，
'''
def fun_a(x,y,z):
    print("x:{},y:{},z:{}".format(x,y,z))
a=(5,6,7)
fun_a(*a)

'''
对字典进行拆包
    使用两个**即可
        下面是代码展示
'''
def fun_b(xa,xb,xc):
    print("xa:{},xb,{},xc,{}".format(xa,xb,xc))
d = {"xa":40,"xb":52,"xc":50}
fun_b(**d)



























