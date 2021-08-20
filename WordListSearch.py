for line in open('wordlist.txt').readlines(  ):
    for string in line.split(  ):
        # print(word)

        # string = input("Enter string:")
        count = 0
        for i in string:
            count = count + 1

        if string[0:2] == string[count-2:count] :
            print(string)