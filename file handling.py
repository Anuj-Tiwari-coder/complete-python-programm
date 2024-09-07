f= open("hello AT2.txt","rb")   # "b"is used for binary output
R=f.read()
print(R)
f.close()

w= open("hello AT2.txt", "w",)
w.write(" Bhag")
w.close()

w= open("hello AT2.txt", "a",)
w.write(" Bhag")
w.close()

with open("hello AT.txt", "a") as w:
    w.write(" this use by with method")
q= open("hello At.txt")
print(q)

# writelines
f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.write("lines")

# readlines
f= open("myfile2.txt", "r")
while True:
    q= f.readline()
    print(q)
    f.close()

#  seek(), tell() and truncate() functions
f= open("myfile2.txt", "r")
d=f.seek(4) #byte
print(f.tell()) #it show which byte was seeked
data=f.read()
print(d)
print(data)
f.close()

with open("file.txt","w") as f:
    d=f.write("This is truncate()function which helps to add only the given charaters")
    t=f.truncate(50)

with open("file.txt", "r") as f:
    d=f.read()
    print(d)
    f.close()