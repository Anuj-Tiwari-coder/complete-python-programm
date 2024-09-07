# Format Method
letter="My name is {}, I'm from {}"
name="Anuj Tiwari"
Country="India"
print(letter.format(name,Country))
# f.(string name{},{})
print(f"My name is {name}, I'm from {Country}")
# next int.f method
txt="your  price: {price:.1f} rs"
print(txt.format(price= 49.99999))
price= 49.99999
print(f"your  price: {price:.2f} rs")

# Docstring
def square(n):
    '''Take the number n, return the square of n'''
    result = n * n
    print(result)
    return result

square(5)
print(square.__doc__)