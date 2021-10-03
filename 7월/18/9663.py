import sys

sys.stdin = open("input.txt")

def Is_true(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def back(x):
    global answer
    if x == N:
        answer += 1
    else:
        for i in range(N):
            row[x] = i
            if Is_true(x):
                back(x + 1)

answer = 0

N = int(input())

row = [[0] for _ in range(N)]

back(0)

print(answer)