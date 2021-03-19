# 백준 9012 괄호

n = int(input())

result = []
for i in range(n):
	text = input()
	while True:
		if "()" not in text:
			break
		else :
			text = text.replace("()", "") # 문자열 치환하는 함수
	if len(text) == 0:
		result.append("YES")
	else:
		result.append("NO")

for r in result:
	print(r)
