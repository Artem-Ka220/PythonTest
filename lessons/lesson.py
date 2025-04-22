'''Условие
В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут.

Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.

Выведите два целых числа: время окончания урока в часах и минутах.'''

numOfLessons = int(input())

howManyMin = 45 * numOfLessons
howManyBreak = numOfLessons // 2
startTime = 9

if numOfLessons % 2 != 0:
    howManyMin = howManyBreak * 5 + howManyBreak * 15 + howManyMin
else:
    howManyMin = howManyBreak * 5 + (howManyBreak - 1) * 15 + howManyMin
print(startTime + howManyMin // 60, howManyMin % 60)
