# Write a program to swap two numbers without using third variable.
# Take values
num1 = int(input('Enter the number'))
num2 = int(input('Enter the number'))
# condition apply
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
# display result
print(f'the num1 is: {num1} and num2 is: {num2}')