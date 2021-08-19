import hashlib

w = 1
while w <= 1000000000:
    res = 'catch-me-if-you-can+' + str(w)
    # print(res)

    hash_object = hashlib.sha256(res.encode()).hexdigest()
    first_chars = hash_object[0:8]
    # print(hash_object)

    if first_chars == '00000000' :
        print(w)
        print(hash_object)
    
    w += 1