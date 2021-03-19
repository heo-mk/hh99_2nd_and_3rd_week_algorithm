# 백준 1753 최단경로
import sys, heapq
sys.stdin = open('a.txt','rt')

INF = float('inf')
# 입력
V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
route = {}
sort_need = []
for i in range(E):
   u, v, w = map(int, sys.stdin.readline().split())
   if u in route:
      route[u] += [(w, v)]
      # sort_need.append(u)
   else :
      route[u] = [(w, v)]


# 작은 순으로 정렬
# for i in sort_need:
#    route[i] = sorted(route[i])

cost = [INF for i in range(V + 1)]
# 탐색 시작
not_visit = []
cost[start] = 0
heapq.heappush(not_visit, (cost[start], start))
while not_visit:
    weight, search_node = heapq.heappop(not_visit)
    if cost[search_node] < weight:
        continue
    if search_node in route:
        for w, v in route[search_node]:
            if v == search_node:
                continue
            if cost[v] > w + cost[search_node]:
                cost[v] = w + cost[search_node]
                heapq.heappush(not_visit, (cost[v], v))

# # 출력
for i in range(1, V + 1):
    if cost[i] < INF:
        print(cost[i])
    else:
        print("INF")