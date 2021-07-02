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


N = int(input())

a = list(map(int , input().split()))

count = 0

for i in a:
    if check(i):
        count += 1
print(count)
