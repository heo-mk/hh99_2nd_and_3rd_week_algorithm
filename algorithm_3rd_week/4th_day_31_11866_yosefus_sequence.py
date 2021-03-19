import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())   # K = step_gap
queue_initial = deque()
for i in range(1, N+1):
    queue_initial.append(i)

# 요세푸스 수열을 담을 리스트
yosefus_sequence = []

# queue 성질 이용해 요세푸스 수열을 만들기
def yosefus_process(queue, yosefus, step_gap):
    while len(queue):
        queue.rotate(-(step_gap - 1))     3 2
        executed = queue.popleft()
        yosefus.append(executed)
    return yosefus
    
    #  O O X O O Y ... 
    #  X O O Y O O Z ... 
    #  [X]
    #  Y O O Z O O L ... 
    #  [X, Y]
    #  Z O O L O O U ... 
    #  [X, Y, Z] 
    #  L O O M O O N ...
    
    # while len(queue) >= step_gap:
    #     queue.rotate(-(step_gap - 1))  
    #     executed = queue.popleft()
    #     yosefus.append(executed)
        
    # # 문제 있는 코드
    # if len(queue) < step_gap:
    #     for j in range(len(queue)):
    #         remain = queue.popleft()
    #         yosefus.append(remain)

    
result = yosefus_process(queue_initial, yosefus_sequence, K)

# 백준의 출력형식에 맞추는 과정
result = str(result).replace('[','').replace(']','')
print('<{}>'.format(result))
