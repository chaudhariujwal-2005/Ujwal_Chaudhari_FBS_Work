# Write a program to swap two numbers using third variable.
#Take value
num1 = int(input('Enter the number:'))
num2 = int(input('Enter the number:'))
# Condition apply
Temp = num1
num1 = num2
num2 = Temp
# Display Result
print(f'the num1 is: {num1} and num2 is: {num2}')