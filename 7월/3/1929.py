def squrter(x):
    return int(x ** (1/2)) + 1

def prime_number(x):
    for i in range(3 , squrter(x) , 2):
        if x % i == 0:
            return False
    return True

import sys

sys.stdin = open("input.txt")

a , b = map(int , input().split())

if a % 2 == 0:
    answer = list(range(a + 1 , b + 1 , 2))
else:
    answer = list(range(a , b + 1 , 2))

b = squrter(b)
for i in range(3 , b , 2):
    if prime_number(i):
        for j in answer:
            if j % i == 0 and j != i:
                answer.pop(answer.index(j))

for i in answer:
    print(i)

            

