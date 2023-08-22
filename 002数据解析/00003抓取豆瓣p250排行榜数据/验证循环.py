w = 0
for i in range(10):
    w +=25
    s = "https://movie.douban.com/top250?start=%d&filter="%(w)
    print(s)