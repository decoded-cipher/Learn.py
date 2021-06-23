import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def percentage(x, y):
    return (x / y) * 100

def sqareroot(x):
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

ch = 'Y'
while ch == 'Y' or ch == 'y':
    print('\nMENU DRIVEN CALCULATOR\n')
    print('Which operation do you want to perform :')
    print(' 1) Addition \n 2) Subtration \n 3) Multiplication \n 4) Division \n 5) Percentage \n 6) Square-Root \n 7) Power\n')
    choice = input('Enter the index value to perform operation : ')

    if choice in ('1', '2', '3', '4', '5', '7'):
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print('Percentage', "=", percentage(num1, num2))

        elif choice == '7':
            print(num1, "^", num2, "=", power(num1, num2))
    
    elif choice == '6':
        num1 = float(input("Enter the number : "))
        print('Square Root of', num1, "=", sqareroot(num1))

    else:
        print("Invalid Input")
    
    ch = input('Do you want to continue (Y/N) : ')
    if ch == 'N' or ch == 'n':
        break

