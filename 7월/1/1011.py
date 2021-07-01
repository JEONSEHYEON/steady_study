import sys

sys.stdin = open("input.txt")

N = int(input())

def hap(x):
    return (1 + x) * x // 2

for _ in range(N):
    a , b = map(int , input().split())
    foot = 1
    dist = b - a - 1
    count = 1
    while dist:
        if dist >= hap(foot + 1):
            foot += 1
            count += 1
            dist -= foot
        elif dist >= hap(foot):
            count += 1
            dist -= foot
        else:
            foot -= 1
            count += 1
            dist -= foot
    print(count)