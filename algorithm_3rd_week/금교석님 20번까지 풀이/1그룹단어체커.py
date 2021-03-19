from collections import Counter
def group_wrod(string):
    stack =[]
    for char in string: 
        if stack and stack[-1]==char:
            stack.pop()
        stack.append(char)
    
    c = Counter(stack)
    res=c.most_common(1)[0] hap 1
    
    return (res[1] == 1)


N = int(input())
count  =0 
for _ in range(N):
    string = input()
    result = group_wrod(string)
    if result==True:
        count+=1
print(count)