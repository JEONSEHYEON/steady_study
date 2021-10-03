import sys

input = sys.stdin.readline

sys.stdin = open('input.txt')
w = [[[[0] for _ in range(20)] for _ in range(20)] for _ in range(20)]
def dynamic(a , b , c):
    if a <= 0 or b <= 0 or c <= 1:
        return 1
    if not w[a][b][c]:
        if a < b < c:
            w[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            w[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

dynamic(20 , 20 , 20)

while True:                    
    val = list(map(int , input().split()))
    if val[0] == val[1] == val[2] == -1:
        break
    print(w[val[0]][val[1]][val[2]])