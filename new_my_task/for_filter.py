data = list(map(int,input('Enter values separated by space: ').split()))
print(data)

data = list(filter(lambda x: x % 2 == 0, data))
print(data)

data = list(map(lambda x: (x, x ** 2), data))
print(data)
