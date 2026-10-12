# Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)
# Take value
P = float(input('enter the principle:'))
R = float(input('enter the rate of amount:'))
T = float(input('enter the time:'))

SI = (P * R * T) / 100

print('simple interest =', SI)
