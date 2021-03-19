# 백준 1260 DFS와 BFS
from collections import deque

dfs_visit = []
def dfs(info, node):
	if node in dfs_visit:
		return
	else:
		dfs_visit.append(node)
		for i in info:
			if i[0] == node and i[1] not in dfs_visit:
				dfs(info, i[1])

bfs_visit = []
def bfs(info, node):
	queue = deque()
	queue.append(node)
	while queue:
		num = queue.popleft()
		bfs_visit.append(num)
		for i in info:
			if i[0] == num and i[1] not in bfs_visit and i[1] not in queue:
				queue.append(i[1])

info = list()
num, line, start = map(int, input().split())
for i in range(line):
	x, y = map(int, input().split())
	info.append([x, y])
	info.append([y, x])
info.sort()

dfs(info, start)
print(' '.join(map(str, dfs_visit)))
bfs(info, start)
print(' '.join(map(str, bfs_visit)))
