# to check whether the triangle is equilateral, isosceles or scalene triangle
# Equilateraltake value
Equilateral = int(input('Enter a:'))
Isosceles = int(input('Enter b:'))
Scalene = int(input('Enter c:'))

if Equilateral == Isosceles == Scalene:
    print('Equilateral')
elif Equilateral == Isosceles or Isosceles == Scalene or Equilateral == Scalene:
    print('Isosceles')
else:
    print('Scalene')