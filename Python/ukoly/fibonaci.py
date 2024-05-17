
def fibonacci(n):
    prev, fib = 0, 1
    if n == 0:
        return prev
    for _ in range(2, n+1):
        prev, fib = fib, prev + fib
    return fib


print (fibonacci(400))