import sys
input = sys.stdin.readline
import copy

# N : 수열의 길이, M : 뽑아낸 수열의 길이
N, M = map(int, input().split())
visited = []  # 탐색 여부 체크
result = []
def DFS_combination(depth):  # depth는 트리구조의 Level과 같은 것
	# 종료 조건 = depth 깊이만큼 탐색했을때
	if depth == M:
		result.append(copy.deepcopy(visited)) #!! 그냥 visited 를 담으면 메모리를 공유하기 때문에 복제 필요
		return
	for j in range(1, N+1):
		if len(visited) and j < max(visited): # 조건 추가, 증가하는 수열이 되면 
			continue
		if j not in visited:
			visited.append(j)
			print(visited)
			DFS_combination(depth+1)   # 설정한 레벨까지 재귀로 간다.
			visited.pop()
			print(visited)

DFS_combination(0)

print(result)