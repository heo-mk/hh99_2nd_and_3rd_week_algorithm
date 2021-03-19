from heapq import heappop, heappush
import sys
input = sys.stdin.readline

INF = float('inf')
# 정점 갯수 : vertex, 간선 갯수 : connect_line
vertexs, connect_lines = map(int, input().split())
# start : 시작정점
start = int(input())

# 정점간 거리 정보 담을 dict
course = {} 

# 서로 다른 정점 : u, v | u -> v ,  간선길이 : w
for i in range(connect_lines):
    u, v, w = map(int, input().split())
    # 이것들을 course에 저장 : 경로 정보를 담아준다
    if u in course:
        course[u] += [(w, v)]
    else:
        course[u] = [(w, v)]

print(course)

# 측정하기 전에는 모든 거리를 무한대로 설정
distances = [INF for i in range(vertexs+1)]
print(distances)
#  정점들을 저장해가며 거리를 갱신할 용도로 min heap 생성(최소힙)
# 여기 저장될 값들 중에서 최소값이 pop 되므로, 최소값을 찾을 수 있다.
minheap = []
distances[start] = 0
print(distances)
heappush(minheap, (distances[start], start))
print(minheap)

while minheap:
    distance, search_node = heappop(minheap)
    if distances[search_node] < distance:
        continue   # 노드간 거리가 원래 있는 거리보다 더 길면 갱신 안함
    if search_node in course:
        for w, v in course[search_node]:
            if v == search_node:
                continue
            if distances[v] > w + distances[search_node]:   # 정점을 지나서 가는 거리가 더 짧으면
                distances[v] = w + distances[search_node]   # 갱신
                heappush(minheap, (distances[v], v))
                print(minheap)
    print(distances)

for j in range(1, vertexs + 1):
    if distances[j] < INF:
        print(distances[j])
    else:
        print('INF')



# def shortest_distance(graph, start, end):
#     # 시작 정점 -> 각 정점까지 거리 저장할 딕셔너리.
#     # start가 아닌 지점까지 거리는 inf로 초기설정.
#     # 계속 갱신해 갈 부분.
#     distances = {vertex:[float('inf'), start] for vertex in graph}

#     # 시작 정점은 자신과의 거리가 0이므로 0으로 설정.
#     distances[start] = [0, start]

    
    
    


