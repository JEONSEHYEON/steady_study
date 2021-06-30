import sys

sys.stdin = open("input.txt")

def div(i):
    div = []
    while i:
        a = i % 10
        i = i // 10
        div.append(a)
    return div

def check(a):
    cha = a[1] - a[0]
    for i in range(0 , len(a) - 1):
        if cha != a[i + 1] - a[i]:
            return False
    return True
        

N = int(input())
count = 0
for i in range(1 , N + 1):
    ans = div(i)
    if len(ans) == 1:
        count += 1
    elif check(ans):
        count += 1

print(count)

