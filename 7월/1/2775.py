import sys

sys.stdin = open("input.txt")

N = int(input())

for _ in range(N):
    height = int(input())
    wide = int(input())
    first = list(range(1 , wide + 1))
    while height:
        upstair = []
        for i in range(1 , wide + 1):
            upstair.append(sum(first[:i]))
        first = upstair
        height -= 1
    print(upstair[wide - 1])  
