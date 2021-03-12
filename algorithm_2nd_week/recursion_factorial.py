def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f

print(factorial(1))
print(factorial(7))
print(factorial(4))

# def hello():
#     print("hello")
#     hello()
    
# hello()