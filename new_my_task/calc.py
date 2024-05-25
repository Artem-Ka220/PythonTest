def calc(x):
    return x * 10

def math(op, x):
    print(op, x)

math(calc(100), 10)

def sum(a, b):
    return a + b

print(sum(4, 5))

def calc(a, b):
    return a * b

print(calc(4, 5))

def mult(op, a, b):
    print(op(a, b))

mult(calc, 4, 5)

sum = lambda x, y: x + y

print(sum(20, 80))

het(lambda x, y: x + y)
print(het(60, 40))
