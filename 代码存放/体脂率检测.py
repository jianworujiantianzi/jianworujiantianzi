height = float(input('请输入你的身高(m):'))
weight = float(input('请输入你的体重(kg):'))
BMI = weight / (height * height)
print('您的BMI值为%.2f' % BMI)
if BMI < 18.5:
    print('体重过轻')
elif 18.5 <= BMI <= 23.9:
    print('体重正常')
elif 24 <= BMI <= 27:
    print('体重过重')
elif 28 <= BMI <= 32:
    print('体重过胖')
else:
    print('非常肥胖')













































