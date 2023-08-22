import datetime

# 读取数据文件
with open("P:\112", 'r') as f:
    lines = f.readlines()

# 解析数据
data = []
for line in lines:
    parts = line.strip().split('\t')
    uid = int(parts[0])
    bid = int(parts[1])
    ttle = parts[2]
    date = datetime.datetime.strptime(parts[3], '%Y-%m-%d')
    data.append((uid, bid, ttle, date))

# 查询《人间词话》的借阅情况
result1 = [record for record in data if record[2] == '《人间词话》']
print(f'查询《人间词话》的借阅情况：{result1}')

# 查询2016年的借阅情况
result2 = [record for record in data if datetime.datetime(2016, 1, 1) <= record[3] < datetime.datetime(2017, 1, 1)]
print(f'查询2016年的借阅情况：{result2}')

# 查询1084420用户在2016年的借阅情况
result3 = [record for record in data if
           record[0] == 1084420 and datetime.datetime(2016, 1, 1) <= record[3] < datetime.datetime(2017, 1, 1)]
print(f'查询1084420用户在2016年的借阅情况：{result3}')

# 查询2016、2018和2019年的借阅情况
result4 = [record for record in data if record[3].year in {2016, 2018, 2019}]
print(f'查询2016、2018和2019年的借阅情况：{result4}')

# 查询借阅了1103310所借图书的用户
result5 = [record[0] for record in data if any(record[1] == bid and record[2] == '《人间词话》' for bid, _, _, _ in data)]
print(f'查询借阅了1103310所借图书的用户：{result5}')