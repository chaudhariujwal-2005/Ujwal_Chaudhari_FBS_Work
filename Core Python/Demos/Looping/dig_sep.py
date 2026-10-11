# digit sep number
num = int(input('enter number:'))
# apply condition
while(num>0):
    d = num % 10
    print('d:',d) #display result
    num = num // 10
    print('num:',num) #display reuslt