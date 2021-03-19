# 백준 2108 통계학
import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = []
for i in range(n):
	arr.append(int(sys.stdin.readline()))
arr.sort()

# 산술 평균
avg = sum(arr)/n
if avg >= 0:
	avg = int(avg + 0.5) # 내림이기 때문에 0.5를 더하여 반올림 처리
else:
	avg = int(avg - 0.5) # 올림이기 때문에 0.5를 더하여 반올림 처리
print(avg)

#중앙값
mid = len(arr) // 2
print(arr[mid])

# 최빈값
c = Counter(arr).most_common()
second = 0
frequency = 0
find = ''
for i in c:
	if frequency <= i[1]:
		frequency = i[1]
		find = i[0]
		second += 1
	if second == 2:
		break
print(find)

# 범위
b = max(arr) - min(arr)
print(b)
