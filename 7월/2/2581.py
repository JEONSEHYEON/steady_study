import sys

sys.stdin = open("input.txt")

def check(x):
    if x == 1:
        return False
    for i in range(2 , x // 2 + 1):
        if x % i:
            continue
        else:
            return False
    return True


a = int(input())
b = int(input())
min = 10000
count = 0
for i in range(a , b + 1):
    if check(i):
        count += i
        if i < min:
            min = i
if count == 0:
    print(-1)
else:
    print(count)
    print(min)