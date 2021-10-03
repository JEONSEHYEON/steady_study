
N = int(input())

lis = [[0 for _ in range(N)] for _ in range(N)]
count = 1
counter = 1
sero = N // 2
garo = N // 2
states = ['up' , 'right', 'down' , 'left']
state = 'up'
while count < N*N:
    state = states[(count - 1) % 4]
    if state == 'up':
        sero -= count
    elif state == 'right':
        garo += count
    elif state == 'down':
        sero += count
    elif state == 'left':
        garo -= count
    if counter == 1:
        count += 1
        counter = 0
    lis[sero][garo] = count
    print(lis[sero][garo])
    counter += 1

print(lis)