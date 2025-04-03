a = int(input())
b = int(input())
c = int(input())
d = int(input())

if d == b + 2 or d == b - 2:
    if c == a + 1 or c == a - 1:
        print('YES')
    else:
        print('NO')
elif c == a + 2 or c == a - 2:
    if d == b + 1 or d == b - 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
