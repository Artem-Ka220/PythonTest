# b = int(input())
# h = int(input())
# c = float((b * h)/2)
# print(c)

# n = int(input())
# if n >= 1440:
# hour = (n % 1440) // 60
# min = (n % 1440) % 60
# else:
# hour = n // 60
# min = n % 60
# print(hour, min)

# name = input()
# print('Hello, ' + name + '!')

# num = int(input())
# print('The next number for the number %d is %d.' % (num, (num + 1)))
# print('The previous number for the number %d is %d.' % (num, num - 1))

#a = int(input())
#b = int(input())
#f = int(input())
#N = int(input())
#N = N - 1
#print((a * 2 * N) + (2 * b * N) + (f * 2) + a)

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)
