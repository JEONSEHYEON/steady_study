import sys

sys.stdin = open('input.txt')

N , M = map(int , input().split())

star = []

def mark(x):
    s = ''
    for i in range(len(x) - 1):
        for j in range(i+1, len(x)):
            if x[j ] > x[i]:
                s += 'u'
            elif x[j] < x[i]:
                s += 'd'
            else:
                s += 's'
    return s

count = 0

for i in range(N):
    x = list(map(int, input().split()))
    s = mark(x)
    if s in star:
        count += 1
    else:
        star.append(mark(x))

print(count)

