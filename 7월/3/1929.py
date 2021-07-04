def squrter(x):
    return int(x ** (1/2)) + 1

def prime_number(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3 , squrter(x) , 2):
        if x % i == 0:
            return False
    return True

import sys

sys.stdin = open("input.txt")

a , b = map(int , input().split())
if a == 2:
    print(a)
if a % 2 == 0:
    a += 1
for i in range(a , b + 1):
    if prime_number(i):
        print(i)

            

