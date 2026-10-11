# Write a program to reverse three-digit number.
# take values
Number = int(input('Enter the digit:'))
# condition apply
Onens = Number % 10
Tens = (Number // 10) % 10
Hundreds = Number // 100
# display result
print(f'reverse number is: {Onens}{Tens}{Hundreds}')