def fibonacci(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]# def fibonacci(n):
# second method
def fib(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

y = int(input("Enter any value for 'n': "))
print(fib(y))