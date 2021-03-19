# 백준 9663 N-Queen 재도전
import copy

length = int(input())

# 테이블 만들기
table = []
disable = []
for _ in range(length):
	table.append([0] * length)
	disable.append([0] * length)

def check(n, i, value):
	side = 0
	while n < length:
		disable[n][i] += value
		if 0 <= i + side < length:
			disable[n][i + side] += value
		if 0 <= i - side < length:
			disable[n][i - side] += value
		side += 1
		n += 1
global count
count = 0

def queen(n):
	global count
	if n == length:
		count += 1
		return
	for i in range(length):
		if disable[n][i] != 0:
			continue
		else : # 사용 가능할 경우
			check(n, i, 1)
			queen(n + 1)
			check(n, i, -1)

queen(0)
print(count)