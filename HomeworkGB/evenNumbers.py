number = int(input("Введите какое-либо число: "))
print(number)
el = 0
while(el <= number):
    if el % 2 == 0:
        print(el, end = ' ')
    el += 1
