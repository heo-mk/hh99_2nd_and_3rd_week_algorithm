# 백준 11047 동전 0
import sys

n, k = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n):
	arr.append(int(sys.stdin.readline()))

count = 0
i = n - 1
while k > 0:
	if arr[i] <= k:
		count += k // arr[i]
		k = k % arr[i]
	else:
		i -= 1

print(count)
