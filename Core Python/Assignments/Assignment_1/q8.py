# Write a program to convert days into years, weeks and days.
# Take values
Days=int(input('Enter days:'))
# Perform
Years=Days//365
Remaining=Days%365
Weeks=Remaining//7
Remaining_Days=Weeks%7
# Display Result
print(f'your years:{Years},week is :{Weeks} and Days is:{Remaining_Days}')