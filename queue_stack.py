# def palindrome(s):  # s: string
#     queue = []
#     stack = []
    
#     for x in s:
#         if x.isalpha():
#             queue.append(x.lower())
#             stack.append(x.lower())
    
#     while queue:   # queue에 문자가 남아 있는 동안
#         if queue.pop(0) != stack.pop():
#             return False
    
#     return True

# print(palindrome('Wow'))
# print(palindrome("Madam, I'm Adam."))
# print(palindrome("Madam, I am Adam."))


def another_palindrome(s):
    check = True
    while True:
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]:
                check = False
                break
            
    return check

print(another_palindrome('Wow'))
print(another_palindrome("Madam, I'm Adam."))
print(another_palindrome("Madam, I am Adam."))