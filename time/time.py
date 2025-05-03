'''hour = int(input())
min = int(input())
interval = int(input())

hour = (interval // 60 + hour) % 24
min = interval % 60 + min
if (min > 60):
    min = min % 60
    hour = hour + 1

print(f'{hour:02d}:{min:02d}')'''

hour = int(input())
minutes = int(input())
interval = int(input())

all_minutes = hour * 60 + minutes + interval
hour = (all_minutes // 60) % 24
minutes = all_minutes % 60

print(f'{hour:02d}:{minutes:02d}')
# print(f'{hour:0>2}:{min:0>2}')
