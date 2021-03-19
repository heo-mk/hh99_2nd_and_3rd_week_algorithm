# 9184 신나는 함수 실행
dic = {}

def w(a, b, c):
	s = str(str(a)+'-'+str(b)+'-'+str(c))
	if s in dic:
		return dic[s]
	if a <= 0 or b <= 0 or c <= 0:
		return 1
	if a > 20 or b > 20 or c > 20:
		dic[s] = w(20, 20, 20)
		return dic[s]
	if a < b and b < c:
		dic[s] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
		return dic[s]
	else:
		dic[s] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
		return dic[s]

result = []
while True:
	a, b, c = map(int, input().split())
	if a == -1 and b == -1 and c == -1:
		break
	s = str(str(a)+'-'+str(b)+'-'+str(c))
	dic[s] = w(a,b,c)
	result.append([a,b,c])

for r in result:
	s = str(r[0])+'-' + str(r[1]) + '-' + str(r[2])
	print("w(" + str(r[0]) + ", " + str(r[1]) + ", " + str(r[2]) + ") = " + str(dic[s]))

