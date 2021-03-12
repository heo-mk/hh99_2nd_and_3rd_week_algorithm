N = int(input()) # 총 갯수 
li = [] # 인풋값을 순서대로 담을 배열
stack = [] # 스택으로 활용할 배열
ans = [] # push/pop을 기록할 배열

# N개의 인풋을 li에 저장하기
for _ in range(N):
    li.append(int(input()))

# 인덱스로 현재 숫자 관리
index = 1

for i in range(N):
    if li[i] >= index:
        while index <= li[i]:
            stack.append(index)
            ans.append("+")
            index += 1
        stack.pop()
        ans.append("-")
    else:
        if len(stack) != 0 and stack[-1] == li[i]:
            stack.pop()
            ans.append("-")

# 스택이 깔끔하게 비워지지 않은 경우: 불가능 (NO 출력)
if len(stack) != 0:
    print("NO")
else: # 스택이 비워짐: 진행한 push/pop 연산 순서대로 출력
    for each in ans:
        print(each)