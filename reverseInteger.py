import time
start = time.time()
timecount = time.time() - start

def reverse(n):
    d = 0
    rev = 0
    while(n>0):
        d = n%10
        n = int(n/10)
        rev = rev*10+d
    return rev
x = int(input("Enter the number:"))
r = reverse(x)
print(x)
print(r)



print(timecount)
