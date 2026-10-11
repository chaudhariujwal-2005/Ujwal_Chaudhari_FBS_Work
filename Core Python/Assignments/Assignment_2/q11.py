# Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.
# take values
amount = int(input('enter the amount:'))
# apply condition
n2000 = amount // 2000
amount = amount % 2000

n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10
# display result
print('2000 notes =',2000)
print('500 notes =', 500)
print('100 notes =',100)
print('50 notes =',50)
print('20 notes =',20)
print('10 notes =',10)