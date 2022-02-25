import random

# Creat random number
num = random.randint(1, 10)
def gusees():

    your_num = int(input('Your number: '))



    if your_num != num:
        print('your number is not true :(')
        if your_num > num:
            print('number is littel')
        else:
            print('number is biger')
    else:
        print('WIN :)')
        return True

while True:
    gusees()
    if gusees():
        break

