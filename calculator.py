# This part of the code defines a function
def multiply(a,b):
    return a * b

def add(a,b):
	return a + b

def subtract(a,b):
	return a - b

def divide(a,b):
	return a / b

def square(a):
	return a ** 2

def cube(a):
	return a ** 3 

def sqaure_n_times(number,n):
	return number ** n

print("I'm going use the calculator functions to multiply 5 and 6")


# This part of the code then calls that function and assigns the variable x to its return value
x = multiply(5,6)


# This prints x to the terminal for humans to read
print(x)

print("I'm going use the calculator functions to add 5 and 6")
y = add(5,6)
print(y)

print("I'm going use the calculator functions to subtract 5 and 6")
z = subtract(5,6)
print(z)

print("I'm going use the calculator functions to divide 5 and 6")
q = divide(5,6)
print(q)

print("I'm going use the calculator functions to square 5")
r = square(5)
print(r)

print("I'm going use the calculator functions to cube 5")
s = cube(5)
print(s)

print("I'm going to square 5 6 times")
w = sqaure_n_times(5,6)
print(w)