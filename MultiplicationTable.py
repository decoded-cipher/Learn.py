x = int(input('\nEnter a Number : '))
print('\nMultiplication table of ' + str(x) + ' is :')

i = 1
while i <= 10:
    res = i*x

    print(str(i) + ' x ' + str(x) + ' = ' + str(res))
    i += 1