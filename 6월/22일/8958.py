import sys

sys.stdin = open("input.txt")

N = int(input())
answer = []
ans = []
for i in range(N):
    try:
        ox = input()
        answer.append(ox)
    except:
        pass

for st in answer:
    count = 0
    hap = 0
    for word in st: 
        if word == 'O':
            count += 1
            hap += count
        if word == 'X':
            count = 0
    ans.append(hap)
for i in ans:
    print(i)