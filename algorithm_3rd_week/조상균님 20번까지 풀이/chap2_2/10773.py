# 백준 10773 제로

n = int(input())

stack = []
for i in range(n):
	num = int(input())
	if num == 0:
		if stack:
			stack.pop()
	else:
		stack.append(num)

print(sum(stack))
