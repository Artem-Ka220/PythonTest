data = list(map(int,input("Enter values separated by spaces: ").split()))
print(data)

def where(c, col):
    return [x for x in col if c(x)]

data = '1 2 3 5 8 15 23 38'.split()
new_list = list(map(int, data))
new_list = where(lambda x: x % 2 == 0, new_list)
print(new_list)
new_list = list(map(lambda x: (x, x ** 2), new_list))
print(new_list)

new_data = [i for i in range(0, 10)]
print(new_data)

new_data = list(filter(lambda x: x % 2 == 0, new_data))
print(new_data)
