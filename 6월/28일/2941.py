import sys

sys.stdin = open("input.txt")

s = input()
croatia = ['c=' , 'c-' , 'dz=' , 'd-' , 'lj' , 'nj' , 's=' , 'z=']
count = 0
top = 0
while s:
    if s[top : top + 3] in croatia:
        s = s[top + 3 :]
        count += 1
    elif s[top : top + 2] in croatia:
        s = s[top + 2 :]
        count += 1
    else:
        s = s[top + 1 :]
        count += 1

print(len(s) + count)

