# Write a program to accept distance in km and convert it into meters and centimeters both.
# Take value
KM = float(input('enter the distance in km:'))

M = KM * 1000
C = KM * 100000

print('meters:', M)
print('centimeter:', C)
