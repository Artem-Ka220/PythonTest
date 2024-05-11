max_number = 0
while True:
    enter_num = int(input("Enter any number: "))
    if max_number < enter_num:
        max_number = enter_num
    elif enter_num == 0:
        print(max_number)
        break
