# Write a program to input any alphabet and check whether it is vowel or consonant.
# Take vlaues
alphabet = input('enter the alphabet:')
# apply if condition
vowel = ('A,a,E,e,I,i,O,o,U,u:')
if(alphabet in vowel):
# display result
    print('the alphabet is vowel:')
else: 
    print('the alphabet is consonant:')