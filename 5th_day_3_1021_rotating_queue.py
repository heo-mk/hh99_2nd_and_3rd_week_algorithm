from collections import deque

N, M = map(int, input().split())

qu = deque()
for i in range(1, N+1):
    qu.append(i)

target_numbers = list(map(int, input().split()))

# for j in range(M):
#     target_number.append(int(input()))

cnt = 0
for k in target_numbers:
    b = qu.index(k)

    if b > (len(qu) - 1)//2:
        move_n = (len(qu) - 1) - b + 1
        for m in range(move_n):
            qu.rotate(1)
        qu.popleft()
        cnt += move_n
    elif b < (len(qu) - 1)//2:
        move_n = b
        for m in range(move_n):
            qu.rotate(-1)
        qu.popleft()
        cnt += move_n
    elif b == (len(qu) - 1)//2:
        move_n = b
        for m in range(move_n):
            qu.rotate(-1)
        qu.popleft()
        cnt += move_n
    print(qu)
    print(cnt)
        
print(cnt)
    
