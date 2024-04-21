age = int(input("Укажите ваш возраст: "))
if 0 < age <= 14:
    print("Вы совсем ещё ребенок!")
elif 14 < age <= 18:
    print("Вы подросток!")
elif 18 < age <= 30:
    print("Вы юноша!")
elif 30 < age <= 60:
    print("Вы взрослый!")
else:
    print("Вы пенсионер!")

    
