#WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic
#Take values
Basic = int(input('Enter the Basic:'))
# Condition apply
DA = Basic * 10 / 100
TA = Basic * 10 / 100
HRA = Basic * 10 / 100
Total_Salary = Basic + DA + TA + HRA
TA = Total_Salary
# Display Result
print("The total salary of employee is ;",TA)

