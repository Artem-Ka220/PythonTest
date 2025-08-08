'''
Кто пойдёт первым? В настольных играх очередность
часто определяется жребием, но мы будем использовать порядок букв!

Давайте сравним имена игроков лексикографически
и с помощью условных операторов определим, кто начнёт игру.

Формат ввода
Три имени игроков, каждое из которых записано с новой строки.

Формат вывода
Имя игрока, который будет ходить первым.
'''
name_one = input()
name_two = input()
name_three = input()

if name_one < name_two and name_one < name_three:
    print(name_one)
elif name_one > name_two and name_two < name_three:
    print(name_two)
else:
    print(name_three)
