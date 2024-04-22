def new_my_function(lst):
    words_2 = []
    for i in lst:
        if i[0] == 'a':
            words_2.append(i)
    return words_2

words = ['apple', 'advertisment', 'picture', 'house', 'adventure', 'hedgehog', 'iterable']
print(words)
new_list = new_my_function(words)

print(new_list)
