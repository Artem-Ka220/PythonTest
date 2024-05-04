def fibo(any_number):
    if any_number in [1, 2]:
        return 1
    return fibo(any_number - 1) + fibo(any_number - 2)

list = []
for i in range(1, 10):
    list.append(fibo(i))
print(list)
