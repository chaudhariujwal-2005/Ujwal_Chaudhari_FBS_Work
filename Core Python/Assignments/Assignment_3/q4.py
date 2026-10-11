# to input all sides of a triangle and check whether triangle is valid or not
Angle_1 = int(input('enter the angle1:'))
Angle_2 = int(input('enter the angle2:'))
Angle_3 = int(input('enter the angle3:'))
# condition
Angle = Angle_1 + Angle_2 + Angle_3
# display result
if(Angle is 180):
    print('the Angle is valid')
else:
    print('the Angle is not valid')