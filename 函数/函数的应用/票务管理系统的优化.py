'''
函数版票务管理系统
    1.查询所有的车票信息
    2.根据开始站点，目的站点出行查询车票信息
    3.购买车票
    4.退票
    5.退出系统

'''
#使用函数打印信息
def print_menu ():
    print("="*50)
    print("1.查询所有的车票信息")
    print("2.根据开始站点，目的站点，出行日期查询车票信息")
    print("3.购买车票")
    print("4.退票")
    print("5.退出系统")
    print("="*50)

print_menu()  #调用函数
def listto ():     #把一个数值在列表里面循环

    for listtomi in list:
        print(listtomi)
#定义一个函数将输入的值进行比对
def listtodo (kaishi,mudi,riqi):
    #查询车票
    for listgood in list:
        if listgood["开始站点"] == kaishi and listgood["目的站点"] == mudi and listgood["日期"] == riqi:
            #return把车票信息返回给调用者，立马结束当前函数的运行
            return listgood
        #如果没有找到返回一个空对象
    return None

def goumai(kaishi,mudi,riqi):
    #购买车票
    #查询车票
    sss=listtodo(kaishi,mudi,riqi)
    if sss is None:
        print("没有对应的车票信息")
    else:
        sss["数量"]-=1
        print("购票成功:")
        print("您购买的车票信息为",sss)
def tuipiao(a,b,c,d):
    #查询是否有对应的车票
    sss=listtodo(a,b,c)
    #判断是否为空
    if sss is None:    #如果没有对应的信息则增加一条新的信息
        list.append({"开始站点":a,"目的站点":b,"日期":c,"票价":"800","数量":d},)
    else:
        #如果找到车票信息则需要找到对应的车票信息数量加1
        sss["数量"]+=d
    print("退票成功")
    print("您退的车票信息为:",sss)

#定义一个全局变量
list = [
    {"开始站点":"广州","目的站点":"北京","日期":"20190909","票价":"800","数量":5},
    {"开始站点":"a","目的站点":"b","日期":"c","票价":"800","数量":5},
    {"开始站点":"广州","目的站点":"北京","日期":"20190909","票价":"800","数量":5},
    {"开始站点":"上海","目的站点":"北京","日期":"20190909","票价":"800","数量":5},

]
while True:
    model = int(input("请输入你要操作的序号"))
    if model == 1:
        print("1.查询车票的信息")
        listto()
    elif model == 2:
        print("2.根据开始站点，目的站点，出行日期查询车票信息")
        a = input("请输入你的开始站点")
        b = input("请输入你的目的站点")
        c = input("请输入您的出发日期")
        hhh = listtodo(a,b,c)
        if hhh is None:
            print("没有对应的车票信息")
            print("="*50)
        else:
            print("车票信息:",hhh)
            print('='*40)
    elif model == 3:
        print("3.购买车票")
        a = input("请输入你的开始站点")
        b = input("请输入你的目的站点")
        c = input("请输入您的出发日期")
        goumai(a,b,c)
    elif model == 4:
        print("4.退票")
        #分两种情况，一种是如果要退的车票里面存在信息数量直接加一就可
        #另一种是，如果没有则新增一条车票信息
        a = input("请输入你的开始站点")
        b = input("请输入你的目的站点")
        c = input("请输入您的出发日期")
        d = int(input("请输入你的退票数量"))
        tuipiao(a,b,c,d)
    elif model == 5:
        print("5.退出系统")
        break
    else:

        print("输入的信息有误请重新输入")










































