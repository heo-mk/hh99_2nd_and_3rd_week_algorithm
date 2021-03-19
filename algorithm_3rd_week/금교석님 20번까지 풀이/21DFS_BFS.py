from collections import defaultdict
from collections import deque

def DFS(vertex,visited):
    if visited[vertex]==True:
        return
    visited[vertex] = True
    print(vertex,end=" ")
    for v in MAP[vertex]:
        DFS(v,visited)
        
def BFS(vertex,visited):
    queue = deque([vertex])
    while queue:
        v=queue.popleft()
        visited[v]=True
        print(v,end=" ")
        for v in MAP[v]:
            if visited[v]==False:
                visited[v]=True
                queue.append(v)
    
#선언
MAP = defaultdict(list)
N,M,V = map(int,input().split())


#초기화 하기
for _ in range(M):
    v1,v2 = map(int,input().split())
    MAP[v1].append(v2)
    MAP[v2].append(v1)
# 정렬하기
for key,value in MAP.items():
    value.sort()
    
visited = [False]*(N+1)
DFS(V,visited)

print() #프린트 초기화

visited = [False]*(N+1)
BFS(V,visited)


