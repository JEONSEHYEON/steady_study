import sys
sys.stdin = open("input.txt")

x , y = map(int , input().split())
chess = []
for i in range(x):
    a = list(input())
    chess.append(a)
row = 0
col = 0

def switch(w):
    if w == 'B':
        return 'W'
    else:
        return 'B'
def rebuild(x):
    count = 0
    for i in range(7):
        if x[i][0] == x[i + 1][0]:
            x[i+1][0] = switch(x[i][0])
            count += 1
    for line in x:
        for i in range(7):
            if line[i] == line[i + 1]:
                line[i + 1] = switch(line[i])
                count += 1
    return count

small = 64
    
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
    # for i in check:
    #     print(i)
    # print('\n')
    hap = rebuild(check)
    check[0][0] = switch(check[0][0])
    w = min(hap , 64 - hap)
    if w  < small:
        small = w

print(small)