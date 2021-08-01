import random
import string

letter = string.ascii_letters
number = string.digits
punctuation = string.punctuation

def standard():
    temp = random.sample(letter, 8)
    password = "".join(temp)
    return password

def secure():
    temp = random.sample(letter + number, 16)
    password = "".join(temp)
    return password

def ultra():
    temp = random.sample(letter + number + punctuation, 32)
    password = "".join(temp)
    return password

ch = 'Y'
while ch == 'Y' or ch == 'y':
    print('\nWELCOME TO INOVUS PASSWORD GENERATOR \nThe World\'s Best Password Generator\n')
    print('SELECT YOUR PREFERED MODE :\n1) STANDARD (Low Security) \n2) SECURE (Medium Security) \n3) ULTRA (High Security) \n')
    choice = input('ENTER YOUR PREFFERED MODE : ')

    if choice in ('1', '2', '3'):
        
        if choice == '1':
            print('\nYour STANDARD Password is : INO_', standard())

        elif choice == '2':
            print('\nYour SECURE Password is : INO_', secure())
        else:
            print('\nYour ULTRA SECURE Password is : INO_', ultra())
    else:
            print("Invalid Input")
        
    ch = input('\nDo you want to continue (Y/N) : ')
    if ch == 'N' or ch == 'n':
        break
