n = int(input())
inp = []       # input 값
st = []       # 스택 규칙으로 숫자를 넣고 뺄 리스트
result = []   # +, - 표시 넣을 리스트
new_seq = True


for i in range(n):
    inp.append(int(input()))

# 인덱스로 현재 숫자 관리
count = 1
    
for i in range(n):
    if inp[i] >= count:
        while count <= inp[i]:
            st.append(count)     # data = 4 이면 네번 push, 네번 +
            result.append('+')
            count += 1           # stack에 push 하는 횟수
        
        st.pop()
        result.append('-')       
    
    else:
        if len(st) != 0 and st[-1] == inp[i]:         # stack의 가장 윗부분과 입력값이 같다면 pop
            st.pop()              
            result.append('-')

# stack이 비워지지 않을 경우
if len(st) != 0:
    print('NO')
else:
    for k in result:
        print(k)



