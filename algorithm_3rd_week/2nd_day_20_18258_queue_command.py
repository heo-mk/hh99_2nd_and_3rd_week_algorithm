import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
queue = deque()

def push(x):
    queue.append(x)

def pop():
    if len(queue) == 0:
        return -1
    else:
        return queue.popleft()

def size():
    length = len(queue)
    return length

def empty():
    if len(queue) == 0:
        return 1
    else:
        return 0
    
def front():
    if len(queue) != 0:
        return queue[0]
    else:
        return -1
    
def back():
    if len(queue) != 0:
        return queue[-1]
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
    elif order == "front":
        print(front())
    elif order == "back":
        print(back())       


