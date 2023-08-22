def print_menu():
    print("=" * 50)
    print("1.查询所有的车票信息")
    print("2.根据开始站点，目的站点，出行日期查询车票信息")
    print("3.购买车票")
    print("4.退票")
    print("5.退出系统")
    print("=" * 50)
print_menu()
def listto ():     #把一个数值在列表里面循环

    for listtomi in list:
        print(listtomi)
def listtodo(kaishi, mudi, riqi):
    # 查询车票
    for listgood in list:
        if listgood["开始站点"] == kaishi and listgood["目的站点"] == mudi and listgood["日期"] == riqi:
            # return把车票信息返回给调用者，立马结束当前函数的运行
            return listgood
    # 如果没有找到返回一个空对象
    return None
def goumai(kaishi, mudi, riqi):
    # 购买车票
    # 查询车票
    sss = listtodo(kaishi, mudi, riqi)
    if sss is None:
        print("没有对应的车票信息")
    else:
        sss["数量"] -= 1
        print("购票成功:")
list = [
    {"开始站点":"广州","目的站点":"北京","日期":"20190909","票价":"800","数量":5},
    {"开始站点":"北京","目的站点":"广州","日期":"20190909","票价":"800","数量":5},
    {"开始站点":"广州","目的站点":"北京","日期":"20190909","票价":"800","数量":5},
    {"开始站点":"a","目的站点":"b","日期":"c","票价":"800","数量":5},

]
while True:
    model = input("请输入你要操作的序号")
    if model == "1":
        print("1.查询车票的信息")
        listto()
    elif model == "2":
        print("2.根据开始站点，目的站点，出行日期查询车票信息")
        a = input("请输入你的开始站点")
        b = input("请输入你的目的站点")
        c = input("请输入您的出发日期")
        hhh = listtodo(a, b, c)
        if hhh is None:
            print("没有对应的车票信息")
            print("=" * 50)
        else:
            print("车票信息:", hhh)
            print('=' * 40)
    elif model == "3":
        print("3.购买车票")
        a = input("请输入你的开始站点")
        b = input("请输入你的目的站点")
        c = input("请输入您的出发日期")
        goumai(a, b, c)
    elif model == "4":
        print("4.退票")
    elif model == "5":
        print("5.退出系统")
        break
    else:
        print("输入的信息有误请重新输入")