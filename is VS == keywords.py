# is key is use as equal object , same as == operator
a= "this is a"
b= "this is b"

print("this is (== operators): ",{a==b}) # exact location of object in memory
print("this is (is keyword): ",{a is b}) # exact location of object in memory
print(a,":", {a is a})
print(b ,":",{b == b})