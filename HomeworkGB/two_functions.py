def new_function():
    new_lst = []
    while True:
        any_number = int(input('Enter any number:'))
        if any_number < 0:
            break
        else:
            new_lst.append(any_number)
    return new_lst

def func(lst):
    number = 1
    for i in lst:
        number = number * i
    return number

numbers = new_function()
print(numbers)

print(func(numbers))
