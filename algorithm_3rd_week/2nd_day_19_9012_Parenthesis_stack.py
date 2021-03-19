import sys
input = sys.stdin.readline
T = int(input())

def is_parenthesis_pairs(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":       
            stack.append(i)
        elif string[i] == ")":   
            if len(stack) == 0:  # 앞쪽의 여는 괄호가 닫힌 괄호를 만나 사라졌다거나 앞에서 여는 괄호가 없었다는 뜻   
                return 'no'
            else:
                stack.pop()
        # print(stack)
    
    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'
        
for i in range(T):
    inp = input()
    print(is_parenthesis_pairs(inp))

# 문제점은 출력초과