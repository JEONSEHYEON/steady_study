import sys

sys.stdin = open('input.txt')

print(ord('A'))
print(ord('Z'))

print(ord('2'))
print(ord('0'))

N , B = input().split()
B = int(B)
N = N[::-1]
hap = 0
for i in range(len(N)):
    try:
        k = int(N[i])
    except:
        k = ord(N[i]) - 55
    hap += (B ** i) * k


print(hap)