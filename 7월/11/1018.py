import sys
sys.stdin = open("input.txt")

x , y = map(int , input().split())
chess = []
for i in range(x):
    a = list(input())
    chess.append(a)
row = 0
col = 0
min = 64
def rebuild(x):
    
while True:
    check = []
    if row + 8 > y:
        col += 1
        row = 0
    if col + 8 > x:
        break
    for i in range(col , col + 8):
        check.append(chess[i][row : row + 8])
    row += 1
    hap = rebuild(check)