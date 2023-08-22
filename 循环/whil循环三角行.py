#原理
'''
原理
print('*',end='')
print()
print('*',end='')
print('*',end='')
print('*',end='')
print()
print('*',end='')
print('*',end='')
print('*',end='')
print('*',end='')
print()
'''
aa = 1
while aa <= 3:
    bb = 1
    while bb<=aa:
        print('*',end='')
        bb+=1
    aa += 1
    print()