# 백준 2667 단지번호붙이기

# 입력
n = int(input())
table = []
for i in range(n):
	table.append(list(map(int, (list(input())))))

danji = 2
global count
count = {}

def check(loc_x, loc_y):
	global count
	x = [0,0,1,-1]
	y = [1,-1,0,0]
	for i in range(4):
		a = loc_x + x[i]
		b = loc_y + y[i]
		if 0 <= a < n and 0 <= b < n and table[a][b] == 1:
			table[a][b] = danji
			count[danji] += 1
			check(a, b)


for i in range(n):
	for j in range(n):
		if table[i][j] == 1:
			count[danji] = 1  # 단지에 포함된 건물 수
			table[i][j] = danji
			check(i, j)
			danji += 1

print(len(count))
result = list(count.values())
result.sort()
for r in result:
	print(r)