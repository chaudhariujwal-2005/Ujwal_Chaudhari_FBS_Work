# Write a program to calculate profit or loss.
# take Value
CP = int(input('enter CP:'))
SP = int(input('enter SP:'))

if (CP>SP):
    print('profit:',SP-CP)
else:
    print('loss:',CP-SP)