n = int(input())
m = int(input())
k = int(input())

if m * n < k:
    print('NO')
elif k % n == 0 or k % m == 0:
    print('YES')
else:
    print('NO')
