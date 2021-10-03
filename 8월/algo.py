import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

def search(n_list , x, a, b):
    if a > b:
        return 0
    num = (b + a) // 2
    if n_list[num] == x:
        return 1
    elif n_list[num] < x:
        search(n_list, x, num + 1 , b)
    else:
        search(n_list, x, a, num - 1)

N = int(input())

n_list = list(map(int, input().split()))

n_list.sort()
M = int(input())

m_list = list(map(int , input().split()))

for i in m_list:
    print(search(n_list, i, 0, N - 1))