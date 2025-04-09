N = int(input())
M = int(input())
x = int(input())
y = int(input())

mn = x

if x == 0 or y == 0:
    mn = 0
elif N > M:
    M = min(x, M - x)
    N = min(y, N - y)
    if M < N:
        mn = M
    else:
        mn = N
elif N < M:
    N = min(x, N - x)
    M = min(y, M - y)
    if N < M:
        mn = N
    else:
        mn = M
print(mn)
