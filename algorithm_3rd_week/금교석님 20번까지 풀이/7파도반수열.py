def Dp(N):
    dp_arr =[0,1,1,1,2,2]
    for i in range(5,N+1):
        num = dp_arr[i]+dp_arr[i-4]
        dp_arr.append(num)
    return dp_arr[N]

T = int(input())
for _ in range(T):
    N = int(input())
    print(Dp(N))    