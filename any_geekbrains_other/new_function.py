def fun(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)

your_num = int(input("Введите ваше число: "))
fun(your_num)
