# creating set
# set does not consider the repeated value
s={1,2,3,4,5,6,7,8,9,0,1,4,5}
print(s)
# set cannot be empty if it's empty then is type show as a dict
s={}
print(type(s))
if (type(s)!=set):
    print("set is empty")
else:
    print("set is not empty")
s={1,2,2,3}
print(type(s))
if (type(s)==set):
    print("s is set")
else:
    print("s is not set")

# Methods for sets
s1={1,2,3,4,5,2,3,4,5}
print(s,s1)
print(s.union(s1))
s1.update(s)
s3=s1.intersection(s)
print(s3)
s3.intersection_update(s1)
s1.difference_update(s)
print(s)
s1.symmetric_difference_update(s)
print(s1)
s1.remove(1)
print(s1)
s1.discard(1)
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)
print(s3.isdisjoint(s))
print(s3.issubset(s))
print(s3.issuperset(s))
print(s3.copy())
print(s3)