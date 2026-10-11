# Input 5 subject marks from user and display grade(eg.First class,Second class ..)
#take value
sub_1 = int(input('enter the sub1 marks:'))
sub_2 = int(input('enter the sub2 marks:'))
sub_3 = int(input('enter the sub3 marks:'))
sub_4 = int(input('enter the sub4 marks:'))
sub_5 = int(input('enetr the sub5 marks:'))

total = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
percentage = total / 500 * 100

print('Percentage:', percentage)

if percentage >= 75:
    print('Distinction:')
elif percentage >= 60:
    print('First clss:')
elif percentage >= 50:
    print('Second class:')
elif percentage >= 35:
    print('Pass class:')
else:
    print('fail:')
