# 백준 18258 큐2
from collections import deque
import sys
# 입력
command = []
queue = deque([])
n = int(sys.stdin.readline())
for i in range(n):
	command = list(sys.stdin.readline().split())
	if command[0] == "push":
		queue.append(command[1])
	elif command[0] == "pop":
		if queue:
			print(queue.popleft())
		else:
			print(-1)
	elif command[0] == "size":
		print(len(queue))
	elif command[0] == "empty":
		if queue:
			print(0)
		else:
			print(1)
	elif command[0] == "front":
		if queue:
			print(queue[0])
		else:
			print(-1)
	elif command[0] == "back":
		if queue:
			print(queue[-1])
		else:
			print(-1)

