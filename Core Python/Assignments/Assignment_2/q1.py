# Convert the time entered in hh,min and sec into seconds.
# Take Value
Hours = int(input('Enter the hours:'))
Minutes = int(input('Enter the minute:'))
Second = int(input('Enter the second:'))
# Perform Task
Total  = (Hours * 60 * 60) + (Minutes * 60) + Second
# Display Result
print(f'Hours is:{Hours},Minutes is:{Minutes} and Seconds is:{Second}')
print(f'Total is:{Total}')