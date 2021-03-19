# 백준 10828 스택

# 입력
command = []
n = int(input())
for i in range(n):
	command.append(list(input().split()))

# 동작
stack = []
for c in command:
	if c[0] == "push":
		stack.append(c[1])
	elif c[0] == "pop":
		if stack:
			print(stack.pop())
		else:
			print(-1)
	elif c[0] == "size":
		print(len(stack))
	elif c[0] == "empty":
		if stack:
			print(0)
		else:
			print(1)
	elif c[0] == "top":
		if stack:
			print(stack[-1])
		else:
			print(-1)



