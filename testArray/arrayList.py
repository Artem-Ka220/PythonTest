book = "The Hitchhiker's Giude to the Galaxy"
print(book)

booklist = list(book)
print(booklist)

print(booklist[0:3])

new_word = ''.join(booklist[0:3])
print(new_word)

galaxy = "".join(booklist[-6:])
print(galaxy)

backwards = "".join(booklist[::-1])
print(backwards)

every_other = ''.join(booklist[::2])
print(every_other)

print(''.join(booklist[4:14:]))

print(''.join(booklist[13:2:-1]))
