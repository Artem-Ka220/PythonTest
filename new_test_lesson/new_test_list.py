book = "The Hitchhiker's Guide to the Galaxy."
print(book)
booklist = list(book)
print(booklist)
print(booklist[0 : 3])
print(''.join(booklist[0 : 3]))
print(''.join(booklist[ -7 :]))

backwards = booklist[: : -1]
print(backwards)

every_other = booklist[: : 2]
print(every_other)

word = ''.join(booklist[4 : 14])
print(word)

word_two = ''.join(booklist[13 : 3 : -1])
print(word_two)
