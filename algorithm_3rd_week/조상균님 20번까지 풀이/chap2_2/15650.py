# 백준 15650 N과 M(2)
import copy

arr = []
def func(n, m, before):
	if m == 0:
		if before not in arr:
			arr.append(before)
		return
	for i in range(1, n + 1):
		if i in before or (len(before) and i <= max(before)):
			continue
		else:
			temp = copy.deepcopy(before)
			temp.append(i)
			func(n, m - 1, temp)


n, m = map(int, input().split())

func(n, m, [])

for i in arr:
	print(' '.join(map(str, i)))
