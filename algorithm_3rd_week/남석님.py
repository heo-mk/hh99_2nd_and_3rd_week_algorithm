import sys

memo = {}

def w(a, b, c, memo):
    str_abc = str(a) + str(b) + str(c)

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        result = w(20, 20, 20, memo)
        return result

    if str_abc in memo:
        return memo[str_abc]

    else:
        if a < b and b < c:
            result = w(a, b, c-1, memo) + w(a, b-1, c-1, memo) - w(a, b-1, c, memo)
            memo[str_abc] = result
            return result
        else :
            result = w(a-1, b, c, memo) + w(a-1, b-1, c, memo) + w(a-1, b, c-1, memo) - w(a-1, b-1, c-1, memo)
            memo[str_abc] = result
            return result

while True:
    a, b, c = list(map(int, sys.stdin.readline().split()))
    if a == -1 and b == -1 and c == -1:
        break
    result = w(a,b,c, memo)
    print("w(%d, %d, %d) = %d"%(a, b, c, result))