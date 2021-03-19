# 백준 1753 최단경로
import sys
from heapq import heappop, heappush

INF = 999999999

#입력
V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

route = {} #경로와 비용 정보 저장
cost = [INF] * (V + 1) # 최소 경로 비용 저장

for _ in range(E): # 경로들을 딕셔너리에 저장
	u, v, w = map(int, sys.stdin.readline().split())
	if u in route:
		route[u] += [(v, w)]
	else :
		route[u] = [(v, w)]

visit = [] # 방문할 리스트 힙
heappush(visit, (0,start)) # 시작 노드와 값 입력
cost[start] = 0
while visit: # 팀색해야 할 노드가 있는 경우
	value, node = heappop(visit) # 최소 비용인 노드를 꺼냄
	if node in route:
		for v, w in route[node]:
			if cost[v] > value + w: # 이전 비용 > 경유 직전 비용 + 경유지에서 목적지의 비용
				cost[v] = value + w # 탐색후 작은 값으로 업데이트
				heappush(visit,(cost[v], v))

for i in range(1, V + 1):
	if cost[i] == INF:
		print("INF")
	else:
		print(cost[i])