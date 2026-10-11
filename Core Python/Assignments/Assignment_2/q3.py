# Convert distant given in feet and inches into meter and centimeter.
# Take Values
Foot = int(input('Enter the foot:'))
Inch = int(input('Enter the inch:'))
# Perform Task
Meter = Foot * 0.1458 + Inch * 0.0258
Centimeter = Meter * 100
# Display Result
print('Meter =', Meter)
print('Centimeter =',Centimeter)