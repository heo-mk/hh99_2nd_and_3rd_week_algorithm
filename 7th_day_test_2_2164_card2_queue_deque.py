# deque 모듈 사용
from collections import deque
N = int(input())

# 1부터 N의 정수가 원소인 queue 만들기
qu = deque()
for i in range(1, N+1):
    qu.append(i)
    print(qu)

print()   
# print(qu)
# qu_top = qu.popleft()
# qu.append(qu_top)
# print(qu)

# qu의 원소가 1개 남을 때까지 시행.
while len(qu) > 1:
    qu.popleft()
    if len(qu) == 1:
        break
    qu_after_top = qu.popleft()
    qu.append(qu_after_top)
    print(qu)

print()
print(qu)
        
print(qu[0])
