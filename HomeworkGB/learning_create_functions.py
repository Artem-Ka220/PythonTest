def func(lst):
    for i in lst:
        if i % 2 != 0:
            lst.remove(i)
    return lst

numbers = list(range(10))
num = func(numbers)
print(num)
