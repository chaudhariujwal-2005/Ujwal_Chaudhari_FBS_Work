gender=input('enter gender(F/M):')
age=int(input('enter age:'))
if(gender=='F'):
    if(age>=18):
        print('Girl is eligible for shadi.')
    else:
        print('pehale khana banana sikh lo.')
else:
    if(age>=21):
        print('Boy is eligible for shadi.')
    else:
        print('pehale kamana sikh lo.')                