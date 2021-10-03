import sys

sys.stdin = open('input.txt')


N , M = map(int , input().split())                
a = list(map(int , input().split()))    
len_a = len(a)   
max = 0
for i in range(len_a - 2):                        # 5 6 7 8 9 에서 5 6 7 을 방문
    for j in range(i + 1 , len_a - 1):            # 5 6 7 8 9 에서 6 7 8 을 방문
        for k in range(j + 1 , len_a):            # 5 6 7 8 9 에서 7 8 9 를 방문
            hap = a[i] + a[j] + a[k]              # 고른 3개 숫자를 더함
            if hap <= M and max < hap:            # 만약 합이 최대값보다 작고 이전에 저장했던 가장 큰 합보다 클 때 
                max = hap                         # 최대값을 현재 값으로 갱신해줌

#max(a)

print(max)