# lambda function is use to make a one line def function
# use this when a anonynomus expression want to give for a short period of time
# we can also pass the fun with fun
# it is also use as temporary function

# Example
def avg(x):
    return x*2

print(avg(2))

# now Lambda Fun
sum= lambda X: X+4
cube= lambda X: X*X*X
multiply= lambda X:X*X
div= lambda X: X/X
print(sum(2))
print(cube(2))
print(multiply(2))
print(div(4),"\n")

avg= lambda X,y: (X+y) /2
print("avg",avg(1,2))

def fun(fx, value):
    return 6+ fx(value)
print(fun(multiply,3))

# lambda fun use at when we make more then 3 func in one program