sosu = [0 for _ in range(10001)]

sosu[1] = 1

for i in range(2 , int(10001**(1/2)) +1):
    for j in range(i * 2 , 10001 , i):
        sosu[j] = 1

a = int(input())
d = a // 2
for i in range(d , 1 , -1):
    if sosu[i] == 0 and sosu[a - i] == 0:
        print(i , a - i)
        break
    
    
