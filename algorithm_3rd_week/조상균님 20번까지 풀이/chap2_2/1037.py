# 백준 1037 약수

n = int(input())
arr = list(map(int,input().split()))

arr.sort()
result = arr[0] * arr[-1]

print(result)
# 가장 작은 약수랑 가장 큰 약수를 곱하면 해당 숫자가 됨
