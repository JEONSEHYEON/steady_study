import sys

sys.stdin = open("input.txt")

N = int(input())

musle = list(map(int , input().split()))
da = 0
musle.sort()
if N % 2:
    da = musle.pop()
    front = 0
    back = len(musle) - 1
    while True:
        if musle[front] + musle[back] > da:
            da = musle[front] + musle[back]
        if back - front == 1:
            break
        back -= 1
        front += 1
else:
    front = 0
    back = len(musle) - 1
    while True:
        if musle[front] + musle[back] > da:
            da = musle[front] + musle[back]
        if back - front == 1:
            break
        back -= 1
        front += 1

print(da)



#5 1 9 5 6 3 2
#1 2 3 5 5 6 9
#1 2 3 5 5 6    da = 9

