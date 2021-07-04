import sys

sys.stdin = open("input.txt")

def squrter(x):
    return int(x ** (1/2)) + 1
def prime_number(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3 , x // 2 + 1):
        if x % i == 0:
            return False
    return True

N = int(input())

for i in range(N):
    n = int(input())
    a = n // 2  
    b = n // 2
    while True:
        if prime_number(a) and prime_number(b):
            break
        a -= 1
        b += 1
    print(a , b)