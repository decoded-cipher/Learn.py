
n = int(input("Enter the number of rows : "))
print()

for i in range(0, n):  
    for j in range(0, i + 1):  
        print("* ", end="")       
    print()

rows = n - 1
for i in range(rows + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("* ", end="")  
    print()