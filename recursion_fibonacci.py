# def fibonacci(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
    
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))

def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print(fibonacci(9))
print(fibonacci(8))
print(fibonacci(7))