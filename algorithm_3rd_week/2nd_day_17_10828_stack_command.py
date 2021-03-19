import sys
N = int(sys.stdin.readline().rstrip())
stack = []

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()

def size():
    length = len(stack)
    return length

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0
    
def top():
    if len(stack) != 0:
        return stack[-1]
    else:
        return -1

for i in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    order = cmd[0]
    if order == "push":
        push(cmd[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())     



