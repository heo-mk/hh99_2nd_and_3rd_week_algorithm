N, M = map(int, input().split()) # N = total number of trees, M = Target total lenght of trees
trees_length = list(map(int, input().split()))
max_tree = max(trees_length)

start = 1
end = max_tree

while start <= end:
    mid = (start + end) // 2
    log = 0
    
    for i in trees_length:
        if i >= mid:
            log += i - mid
    
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)