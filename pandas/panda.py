'''Преобразование значений столбца в датафрейм.'''

import pandas as pd

df = pd.DataFrame({
    'age': [25, 30, 35, 40],
    'salary': [1000, 1500, 2000, 2500]
    })

print(df)


def increase_age(x):
    return x + 1


df['age'] = df['age'].apply(increase_age)

print(df)

df['age'] = df['age'] + 1

print(df)
