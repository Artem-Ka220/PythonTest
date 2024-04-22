def new_function(lst, lst_2):
    lst_3 = []
    for i in lst:
        if i in lst_2:
            lst_3.append(i)
    return lst_3

num = [1, 3, 5, 7, 9, 2]
num_2 = [3, 7, 9, 2, 0]
print(num)

print(num_2)

num_3 = new_function(num, num_2)
print(num_3)
