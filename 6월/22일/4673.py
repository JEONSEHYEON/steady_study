def hap(n):
    hap1 = 0
    while n:
        hap1 += n % 10
        n = n // 10
    return hap1


visited = list(range(1 , 10001))
visited[0] = 1
for i in range(1 , 10001):
    check = i + hap(i)
    try:
        visited.remove(check)
    except:
        continue    
for i in visited:
    print(i)