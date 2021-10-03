import sys

sys.stdin = open('input.txt')

while True:
    try:
        t1, t2 = input().split()
    except:
        break
    t1 = list(map(int, t1.split(':')))
    t2 = list(map(int, t2.split(':')))
    count = 0
    while True:
        t1_hap = t1[0] * 10000 + t1[1] * 100 + t1[2]
        if t1_hap % 3 == 0:
            count += 1
        t1[2] += 1
        if t1[2] == 60:
            t1[1] += 1
            t1[2] = 0
        if t1[1] == 60:
            t1[0] += 1
            t1[1] = 0
        if t1[0] == 24:
            t1[0] = 0
        if t1 == t2:
            t1_hap = t1[0] * 10000 + t1[1] * 100 + t1[2]
            if t1_hap % 3 == 0:
                count += 1
            break
    print(count)