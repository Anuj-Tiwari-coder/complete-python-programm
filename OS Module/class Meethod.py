# This Method is use for change class name
class employe:
    company= "Samsung"
    def show(self):
        print(f"Company name: {self.company}\nName of the emp: {self.name}")
    @classmethod
    def change_company(self, new_company):
        self.company = new_company

a = employe()
a.name= "harry"
a.show()
a.change_company("Google")
a.show()
print(employe.company)

# object introspector dir, dict ( is a attributes ) and help Method
# dir show's the all method use for
A= [1,2,3,4]
print(dir(A))
print(A.__class__, A.append(5))
print(A)

# __dict__ is a attribute
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p= person(
    name= "Anuj"
    ,age= 20)
print(p.__dict__)

# help
print(help(str))
print(help(tuple))
help(person)

# using super() function
class start:
    company= "Samsung"
    def __init__(self, name, id):
        self.name = name
        self.id = id
class programmer(start):
    def __init__(self , name , id , post):
        super().__init__(name, id)
        self.post= post

p1=start("Anuj" , 123)
p2=programmer("Kailash", 123435 ,"python")
print(p2.name)
print(p2.id)
print(p2.post)

# this just try with own
class company:
    company= "Samsung"
    def __init__(self, name, id):
        self.name = name
        self.id = id
p=company(name=input("e"),id= int(input("e")))
print(p.company,p.name, p.id)