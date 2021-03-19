import sys

T = int(input())

stack =[]
for _ in range(T):
    log = sys.stdin.readline().rstrip().split(" ")
    command, num = log[0],log[-1]
    if command=="push":
        stack.append(int(num))
    elif command =="pop":
        if stack:
            print(stack.pop())
        else:
            print("-1")
    elif command =="size":
        print(len(stack))
    elif command =="empty":
        if stack:
            print("0")
        else:
            print("1")
    elif command =="top":
        if stack:
            print(stack[-1])
        else:
            print("-1")
        
    
    
    