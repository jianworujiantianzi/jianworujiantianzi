"""
回调函数
    把函数A作为函数B的参数,然后在函数B执行到某一个时机的时候调用函数A，那么我们把函数A
称之为回调函数，
"""
def fdx():
    """发送短信"""
    print("亲爱的我到家了")
def gohome(callback):
    """回家

    """
    print("打出租车回家")
    print("到家了")
    callback()
def chi():
    print("肚子饿了吃点方面面")
'''回调函数'''
gohome(chi)  #传进去的是函数名称不能加括号加括号是函数调用的意思
gohome(lambda:print("在看电影"))  #直接传入参数进去