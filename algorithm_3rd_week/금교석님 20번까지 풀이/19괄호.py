N = int(input())

def is_VPS(log):
    stack =[]
    for char in log:
        if stack and char==")" and stack[-1]=="(":
            stack.pop()
        else:
            stack.append(char)
    return (len(stack)==0) #비어있으면


for _ in range(N):
    log = input()
    if is_VPS(log):
        print("YES")
    else:
        print("NO")