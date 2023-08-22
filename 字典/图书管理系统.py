print("="*30)
print("图书管理系统")
print("查找图书请安1")
print("借阅图书请安2")
print("归还图书请安3")
print("显示全部图书请按4")
print("退出系统请按5")
book = [
    {"名称":"python","数量":10},
    {"名称":"jiav","数量":10},
    {"名称":"c++","数量":10}
]
while True:
    shuru = int(input("请输入你选择的序号"))
    if shuru ==1:
        print("查找图书")
        book_name = input("请输入你要查找的书名")
        for books in book:
            if book_name == books["名称"]:
                print("信息：",books)
                break
        else:
            print("没有找到你需要的图书")
    elif shuru == 2:
        print("借阅图书2")
        book_goodname = input("请输入您要借阅的图书")
        for books in book:
            if book_goodname == books["名称"] and books["数量"] > 0:
                print("恭喜你成功借阅")
                books["数量"] -= 1
                print("你借阅的",end='')
                print(books["名称"],end="")
                print("书籍还有",end='')
                print(books["数量"],end='')
                print('本')
            break
        else:
            print("没有你需要的图书")

    elif shuru == 3:
        print("归还图书")
        a = input("请输入你要归还的书籍")
        for books in book:
            if a == books["名称"]:
                books["数量"] +=1
                print('你已经成功归还书籍',end='')
                print(books["名称"],end='')
                print('还有',end='')
                print(books["数量"],end='')
                print('本')
        else:
            book.append({"名称":a,"数量":1})
            for b in book:
                if a == b["名称"]:
                    print(b)
            print("归还成功")
            print("="*30)

    elif shuru == 4:
        print("以下是全部的图书了")
        for x in book:
            print(x)
    elif shuru == 5:
        print("退出系统")
        break
    else:
        print("输入序号有误")



'''
有问题待解决，问题就是第三归还图书的时候如果该书没有存在则添加一本这个书
可是不存在的这本书如果连续输入两次的话他就输入两次的话，他就会打印两边不存在的

'''














