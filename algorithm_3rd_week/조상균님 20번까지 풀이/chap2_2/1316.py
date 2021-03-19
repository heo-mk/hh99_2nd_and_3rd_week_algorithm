# 백준 1316 그룹단어 체커

#입력
n = int(input())
words = []
for _ in range(n):
	words.append(input())


# 구현
count = 0 # 그룹 단어 갯수
for word in words: # 단어들 하나씩 반복
	dic = {} # 단어 체크, 다음
	before = word[0] # 이전 문자와 같은지 체크하기 위해 사용하는 변수
	group = True # 올바른 그룹 단어인지
	for c in word:
		if c in dic: # 이전에 나온 문자가 있을 경우
			group = False
			break
		elif before != c: # 새로운 문자일 때
			dic[before] = 1 # 이전 문자를 딕셔너리에 담음
			before = c # 이전 문자로 지정
		else: # 이전 문자와 같을 때
			before = c
	if group: # 그룹단어면 카운트 1 증가
		count += 1

# 출력
print(count)

