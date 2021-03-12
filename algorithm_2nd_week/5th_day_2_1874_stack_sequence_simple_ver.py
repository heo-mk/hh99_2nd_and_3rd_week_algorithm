n = int(input())      # 첫 입력 : 수열의 숫자 갯수
stack = []            # stack : 숫자가 스택 규칙으로 들어갔다가(push) 나오는(pop) 스택
count = 0             # stack에 입장-퇴장 반복할 숫자
result = []
determinator = True   # 스택 규칙에 맞는 수열인지 판별한다.

for i in range(n):            # 수열 내 숫자 갯수만큼 반복 입력
    num = int(input())    
    
    while count < num:        # 입력한 num 보다 작은 값까지 스택에 숫자 push
        count += 1            # ex) num = 4 이면 count = 1, 2, 3, 4
        stack.append(count)
        result.append("+")    # push이므로 +
        
    top = stack[-1]           # ex) num = 4, count = 4 일 때, top = stack[-1] = 4 그러므로 top = num
    if top == num:            # 처음 입력한 num과 stack에 마지막으로 입장한 수가 같을 때 
        stack.pop()           # pop으로 빼낸다.
        result.append('-')    # pop이므로 - 
    else:                     # 스택에 마지막으로 push된 숫자가 입력한 값과 다르다는 것은 스택 규칙에 어긋난다.
        determinator = False
        break                 # 스택 규칙에 어긋나므로 더 볼 필요 없음.
    
if determinator == False:     # 스택의 규칙으로 만들 수 없는 수열이다.
    print('No')
else:
    for i in result:          # 스택 규칙에 맞는 수열이라면 result의 +, -를 하나씩 출력
        print(i)