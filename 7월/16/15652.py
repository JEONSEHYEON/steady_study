import sys

sys.stdin = open('input.txt')

def rec(deep):
    if deep == M:
        for j in solve:
            print(j , end=' ')
        print()
        return
    for i in range(1 , N + 1):
        if deep != 0:
            if i < solve[-1]:
                continue
        solve.append(i)
        rec(deep +1)
        solve.pop()


N , M = map(int , input().split())
solve = []
rec(0)