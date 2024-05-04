def new_function(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

your_num = int(input('Введите любое число: '))
print(new_function(your_num))
