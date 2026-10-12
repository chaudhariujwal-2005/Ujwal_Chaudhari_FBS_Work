# Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user:
# Take value
L = float(input('enter length:'))
B = float(input('enter breadth:'))
R = float(input('enter radius:'))

area = (L * B) + (3.14 * R * R / 2)
print('Area =', area)

perimeter = (2 * 1) + B + (3.14 * R)
print('Perimeter =', perimeter)