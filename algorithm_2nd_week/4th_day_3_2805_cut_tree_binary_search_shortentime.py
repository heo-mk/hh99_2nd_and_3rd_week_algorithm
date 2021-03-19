# 이진탐색으로 해결
N, M = map(int, input().split()) # N = total number of trees, M = Target total lenght of trees
trees_length = list(map(int, input().split()))
max_tree = max(trees_length)

start = 1
end = max_tree

# 이진탐색을 자르는 높이를 바꿔 가는 것으로 구현했다.
# 그래서 자르는 높이의 첫 값은 가장 높은 나무의 중간 높이다.
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