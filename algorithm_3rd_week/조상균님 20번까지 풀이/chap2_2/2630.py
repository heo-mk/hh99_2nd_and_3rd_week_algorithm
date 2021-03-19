# 백준 2630 색종이 만들기

def check_blue(table, n, x, y):
	for i in range(x, x+n):
		for j in range(y, y+n):
			if table[i][j] == 0:
				return False
	return True


def check_white(table, n, x, y):
	for i in range(x, x+n):
		for j in range(y, y+n):
			if table[i][j] == 1:
				return False
	return True

def half(table, n, x, y):
	if check_blue(table, n, x, y): # 파란 종이인 경우
		return [0, 1]
	if check_white(table, n, x, y):
		return [1, 0]
	n = n//2
	total = [0, 0]
	box1 = half(table, n, x, y)
	box2 = half(table, n, x + n, y)
	box3 = half(table, n, x, y + n)
	box4 = half(table, n, x + n, y + n)
	total[0] = box1[0] + box2[0] + box3[0] + box4[0]
	total[1] = box1[1] + box2[1] + box3[1] + box4[1]
	return total

# 입력
n = int(input())
table = []
for i in range(n):
	table.append(list(map(int, input().split())))

#실행
result = half(table, n, 0, 0)

print(result[0])
print(result[1])
