def fibo(any_num):
    if any_num in [1, 2]:
        return 1
    return fibo(any_num - 1) + fibo(any_num - 2)

num = int(input('Введите число: '))
for i in range(1, num + 1):
    print(fibo(i), end = ', ')
print()
list = []
for i in range(1, 10):
    list.append(fibo(i))
print(list)
