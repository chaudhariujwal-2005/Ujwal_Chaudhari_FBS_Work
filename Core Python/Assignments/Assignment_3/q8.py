# prompt user to enter userid and password.After verifying userid and password display a 4 digit random number
import random

Userid = input('enter the id:')
Password = input('enter the password:')

if Userid == "ujwal" and "12344" == "12344":
   num = random.randint(1000, 9999)
   print('Captcha:', num)

   user_num = int(input('enter the Captcha:'))

   if user_num == num:
      print('Success')
   else:
      print('Failed')
else:
   print('invalid User id or password')

   