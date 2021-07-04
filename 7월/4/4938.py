import sys
def squrter(x):
    return int(x ** (1/2)) + 1
def prime_number(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3 , squrter(x)):
        if x % i == 0:
            return False
    return True

sys.stdin = open("input.txt")

while True:
    a = int(input())
    if a == 0:
        break
    count = 0
    for x in range(a + 1, 2*a + 1):
        if prime_number(x):
            count += 1
    print(count)
