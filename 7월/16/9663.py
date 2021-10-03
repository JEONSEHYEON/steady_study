import sys

sys.stdin = open('input.txt')

check_list_i = []
check_list_j = []
check_list_ij = []


def check(N):
    for i in range(N):
        for j in range(N):
            if  i in check_list_i:
                return
            if j in check_list_j:
                return
            if [i,j] in check_list_ij:
                return
            

check_list.append([1,2])
j = 1
i = 2
if [j,i] in check_list:
    print(1)