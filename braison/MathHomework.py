print('MathHomework.py')
# Попросить ввести задачу
problem = input('Введите задачу или q для выхода.')

while (problem != 'q'):
    print('Ответ на ', problem, ' - это', eval(problem))
    problem = input("Введите ещё одну задачу или 'q', чтобы выйти: ")
