# x = int(input('\nEnter a Number : '))
# print('\nMultiplication table of ' + str(x) + ' is :')

# i = 1
# while i <= 10:
#     res = i*x

#     print(str(i) + ' x ' + str(x) + ' = ' + str(res))
#     i += 1


x = int(input('\nEnter a Number : '))

num = []
i = 1

if x % 2 == 0:
    print(str(x) + ' is an Even Number :')
    while i <= x:
        if i % 2 == 0:
            num.append(i)
        i += 1
else:
    print(str(x) + ' is an Odd Number :')
    while i <= x:
        if i % 2 != 0:
            num.append(i)
        i += 1

print(num)

for y in num:
    print('\nMultiplication table of ' + str(y) + ' is :')
    w = 1
    while w <= 10:
        res = y * w

        print(str(y) + ' x ' + str(w) + ' = ' + str(res))
        w += 1