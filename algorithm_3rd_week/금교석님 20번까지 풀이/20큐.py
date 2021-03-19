from collections import deque
import sys
T = int(input())

queue =deque([])
for _ in range(T):
    log = sys.stdin.readline().split(" ")
    command, num = log[0],log[-1]
    if command=="push":
        queue.append(int(num))
    elif command =="pop":
        if queue:
            print(queue.popleft())
        else:
            print("-1")
    elif command =="size":
        print(len(queue))
    elif command =="empty":
        if queue:
            print("0")
        else:
            print("1")
    elif command =="front":
        if queue:
            print(queue[0])
        else:
            print("-1")
    elif command =="back":
        if queue:
            print(queue[-1])
        else:
            print("-1")
        