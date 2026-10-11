# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
# take value
gender = input('enter the gender:')
age = int(input('enter the age:'))

if gender == "male" and age >= 21:
    print('eligible for marriage:')
elif gender == "female" and age >= 18:
    print('eligible for marriage:')
else:
    print('not eligible for marriage')