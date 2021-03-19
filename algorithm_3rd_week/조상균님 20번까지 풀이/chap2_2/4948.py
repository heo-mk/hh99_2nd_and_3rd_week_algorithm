# 백준 4948 베르트랑 공준
import sys

# 입력
arr = []
while True:
	num = int(sys.stdin.readline())
	if num == 0:
		break
	else:
		arr.append(num)

# 가장 큰 수의 두배까지 소수 판별 테이블 만들기
max_num = max(arr) * 2 + 1
table = [True] * (max_num)
i, j = 2, 2
while i < (max_num ** 0.5) + 1:
	j = 2
	if table[i]:
		while i * j < max_num:
			table[i*j] = False
			j += 1
	i += 1
table[0] = False
table[1] = False

for i in arr:
	count = 0
	for j in range(i + 1, (i * 2) + 1):
		if table[j] == True:
			count += 1
	print(count)
