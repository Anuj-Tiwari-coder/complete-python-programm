# those object out of the function it's called Global Variable
# Those are inside the functin that value is called Local variable

g= 5 # this is a global variable
print(f"this is Global {g} Variable ")
# use global
def local():
    h= 4
    global x
    x=3
    print(f"this is local {h} Variable")
    print(f"this is after Modify {x} global value")
local()
# we can access the function for Global but can't use local