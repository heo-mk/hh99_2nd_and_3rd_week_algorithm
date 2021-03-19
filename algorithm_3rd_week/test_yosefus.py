n, k = map(int, input().split())
q = [i for i in range(1,n+1)]
print("<",end='')
i = 0

while len(q) > 1:
    i = i+k
    if i > len(q):
        i = i % len(q)
        if i == 0 :
            i = i+ len(q)
    i = i-1
    print(str(q.pop(i)), end=", ")

print("{}>".format(str(q.pop())))

# from sys import stdin
# n, k = map(int, stdin.readline().split())
# arr = [range(1, n+1)]
# idx = 0
# res = []
# while arr:
#     idx += (k - 1)
#     if idx > len(arr) - 1:
#         idx %= len(arr)
#     res.append(arr.pop(idx))
    
# print(res)