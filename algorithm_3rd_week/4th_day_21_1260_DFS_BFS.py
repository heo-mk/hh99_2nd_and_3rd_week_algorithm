import sys
input = sys.stdin.readline
from collections import deque

# N = 정점(vertex)의 갯수, M = 정점을 잇는 선들의 개수, V =  탐색 시작할 정점 번호
N, M, V = map(int, input().split())

vertex_graph = {}
for i in range(N):
    vertex_graph[i+1] = []  # i+1 : key가 1부터 시작해 1,2,3...가 되게 한다.

for j in range(M):
    vertex1, vertex2 = map(int, input().split())
    vertex_graph[vertex1] += [vertex2]
    vertex_graph[vertex2] += [vertex1]

print(vertex_graph)

def DFS(graph, start_vertex):
    stack = [start_vertex]
    visited = []
    while stack:
        current_vertex = stack.pop()
        visited.append(current_vertex)
        for adjacent_vertex in vertex_graph[current_vertex]:
            if adjacent_vertex not in visited:
                # visited.append(adjacent_vertex)
                stack.append(adjacent_vertex)
                # # test.append(adjacent_vertex)
                # break
    return visited 

def BFS(graph, start_vertex):
    queue = [start_vertex]
    visited = []
    while queue:
        current_vertex = queue.pop(0)
        visited.append(current_vertex)
        for adjacent_vertex in vertex_graph[current_vertex]:
            if adjacent_vertex not in visited:
                queue.append(adjacent_vertex)
        # print(visited)
        
    # print(visited)
    # result = set(visited)
    # return result
    return visited

    #     print(visited)
    #     print(test)
        
    # print(visited)
    # result = set(visited)
    # return result

print(DFS(vertex_graph, V))
print()
print(BFS(vertex_graph, V))
print()
