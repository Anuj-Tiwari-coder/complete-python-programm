# Recursion
# by Factorial
def factorial(n):
    if n == 1 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
# we can Also take as like this
# Factorial(5)
# 5 * Factorial(4)
# Factorial(4)
# 4 * Factorial(3)
# Factorial(3)
# 3 * Factorial(2)
# by Fibonacci series
# formula = F(0) = 0(1), F(1)= 1(1)
def fibonacci(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]# def fibonacci(n):
