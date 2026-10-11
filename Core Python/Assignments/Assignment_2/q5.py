# WAP to calculate selling price of book based on cost price and discount.
#Take Value
Cost_Price = int(input('Enter the Book:'))
Discount = int(input('Enter the discount:'))
# Perform Task
Discount = Cost_Price * Discount / 100
Selling_Price = Cost_Price - Discount
#Display Result
print(f'the selling price is {Selling_Price}')
