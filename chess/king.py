a = int(input())
b = int(input())
c = int(input())
d = int(input())

if c == a or c == a - 1 or c == a + 1:
    if d == b or d == b - 1 or d == b + 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
