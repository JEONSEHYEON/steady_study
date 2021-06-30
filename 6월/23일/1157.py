import sys

sys.stdin = open("input.txt")

N = input()
N = N.upper()
alpabet = []
answer = []
for i in range(65 , 91):
    alpabet.append(chr(i))
max = 0
for i in alpabet:
    count = N.count(i)
    if count == max:
        answer.append(i)
    elif count > max:
        answer = []
        answer.append(i)
        max = count

if len(answer) > 1:
    print('?')
else:
    print(answer[0])
