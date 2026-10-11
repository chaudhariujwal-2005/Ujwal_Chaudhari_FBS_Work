# Find the sum of three-digit number.
#Take value
Number = int(input('Enter the digit:'))
#Condition apply
Hundreds = Number // 100
Tens = (Number // 10) % 10
Ones = Number % 10
Sum = Hundreds + Tens + Ones
# Disply result
print(f'Hundreds is: {Hundreds} , Tens is: {Tens} , Ones is: {Ones} and Sum is: {Sum}')