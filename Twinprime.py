def isPrime(n):
    for i in range(2,n):
        if n%i ==0:
            return False

    return  True

for i in range(1,100):
    if isPrime(i) and isPrime(i+2):
        print(i,",",i+2)
        