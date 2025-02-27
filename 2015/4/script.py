from hashlib import md5

input = "iwrupvqb"
i = 1
while True:
    data = input + str(i)
    
    hash = md5(data.encode()).hexdigest()
    if hash.startswith("000000"):
        print(i)
        break

    i += 1