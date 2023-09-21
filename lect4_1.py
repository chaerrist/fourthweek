# type

a = 12
print(type(a))

a = 12.01
print(type(a))

a = "a"
print(type(a))

a = "abcd"
print(type(a))

a = [3, 2, 1]
print(type(a))

# a = 65
# a = "65"
# print(int(a))
# print(str(a))
# print(hex(a))
# print(oct(a))
# print(chr(a))
# print(ord("A"))


print(pow(2, 2))
print(pow(2, 6))
print(pow(3, 4))
print(3 ** 4)

for i in range(6):
    print(i)
    
for i in range(2, 7):
    print(i)
    
a = [3, 5, 5, 9]
print(max(a))
print(min(a))
print(sum(a))

add = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b
print(add(2,3))
print(sub(2,3))
print(mul(2,3))
print(div(2,3))


def add_numb(x, y):
    return x + y
result = add_numb(3, 4)
print(result)


def greet(name):
    print("Hello " + name + " , How are you?")
    
greet("name")

