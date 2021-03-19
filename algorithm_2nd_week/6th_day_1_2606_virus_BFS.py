# 바이러스에 인접한 것은 다 바이러스에 걸린다.
# 어디까지 파고 들어가느냐를 묻는 것이 아니라,
# 얼마나 멀리 번지느냐의 문제이므로 BFS로 접근한다.
n = int(input())       # 컴퓨터 숫자
pairs = int(input())   # 직접 연결된 컴퓨터 쌍의 수
graph = {}             # node 연결 정보

for i in range(n):
    graph[i+1] = []
print(graph)

for i in range(pairs):
    x, y = map(int, input().split())
    graph[x] += [y]    # x 컴에 연결된 y 컴들의 관계를 모두 나타낼 수 있는 방법
    graph[y] += [x]    
print(graph)    
    
def dfs_virus_infection(com_graph, start_com):
    queue = [start_com]
    visited = []
    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for adjacent_com in com_graph[current_node]:
            if adjacent_com not in visited:
                queue.append(adjacent_com)
        print(visited)
    
    print(visited)            
    result=set(visited)
    print(result)        
    return len(result) - 1

print(dfs_virus_infection(graph, 1))