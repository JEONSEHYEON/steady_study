import sys

sys.stdin = open('input.txt')

n, m = map(int, input().split())
solve = []

def BackT(depth , k):
    if depth == m:
        for i in solve:
            print(i, end=' ')
        print()
        return
    for i in range(1, n + 1):
        if i not in solve and i > k:
            solve.append(i)
            BackT(depth + 1 , i)
            solve.pop()

BackT(0 , 0)