
memo ={
}

def w(a,b,c):    
    key = f"{a},{b},{c}"
    if key in memo:
        return memo[key] 
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        memo[key] = w(20,20,20)  
    elif a<b and b<c:
        memo[key]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
    else:
        memo[key]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return memo[key]    


while True:
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    res = w(a,b,c)
    print(f"w({a}, {b}, {c}) = {res}")
    
    