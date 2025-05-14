'''В этой задаче вы продолжите работать с операторами,
но добавим к этому наивную сортировку данных.

Время подвести итоги гонки и объявить победителя!
Длина трассы — 43872 метра, и нам известны
средние скорости трёх фаворитов: Пети, Васи и Толи.
Ваша задача — сравнить результаты гонщиков
и вывести имя победителя.

Формат ввода
В первой строке записана средняя скорость Пети.
Во второй — Васи.
В третьей — Толи.

Формат вывода
Имена победителей в порядке занятых мест.'''

first_athlete = 'Петя'
first_speed = int(input())

second_athlete = 'Вася'
second_speed = int(input())

third_athlete = 'Толя'
third_speed = int(input())

'''if first_speed < second_speed:
    if second_speed > third_speed:
        first_speed, second_speed = second_speed, first_speed
        first_athlete, second_athlete = second_athlete, first_athlete
    else:
        first_speed, third_speed = third_speed, first_speed
        first_athlete, third_athlete = third_athlete, first_athlete
elif first_speed < third_speed:
    first_speed, third_speed = third_speed, first_speed
    first_athlete, third_athlete = third_athlete, first_athlete'''
if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed
    first_athlete, second_athlete = second_athlete, first_athlete

if first_speed < third_speed:
    first_speed, third_speed = third_speed, first_speed
    first_athlete, third_athlete = third_athlete, first_athlete

if second_speed < third_speed:
    second_speed, third_speed = third_speed, second_speed
    second_athlete, third_athlete = third_athlete, second_athlete

print(f"1. {first_athlete}", f"2. {second_athlete}", f"3. {third_athlete}",
      sep=' \n')
