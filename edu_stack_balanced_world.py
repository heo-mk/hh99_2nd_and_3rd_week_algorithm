s = "(())()"

# 왼쪽에서 오른쪽으로 가면서 열린 괄호를 하나씩 저장한다. = stack의 push
# 왼쪽에서 오른쪽으로 가면서 닫힌 괄호가 나올 때마다 열린 괄호를 삭제 한다. = stack의 pop
def is_correct_parenthesis(string):
	# 구현해보세요!
	stack = []
	for i in range(len(string)):
		if string[i] == "(":   # 두 종류 모두 여는 것이라면
			stack.append(i)
		elif string[i] == ")":
			if len(stack) == 0:       # string이 빈 string 이거나, 이전에 (), []가 되어 stack 배열 안에 여는 괄호가 pop()된 상태
				return False
			else:
				stack.pop()
		print(stack)
	
	if len(stack) == 0:
		return True
	else:
		return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!