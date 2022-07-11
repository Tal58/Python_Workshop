def isprime(i):
    count = 0
    for a in range(2,i):
        if i % a !=0:
            count = count
        else:
            count = 1
    if count == 0:
        return True
    else:
        return False

number = int(input("Please enter a number: "))
primelist = []
for i in range(2,number+1):
    if isprime(i):
        primelist.append(i)
print(primelist)