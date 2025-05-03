one_num = int(input())
two_num = int(input())

three_num = (one_num // 100 + two_num // 100) % 10 * 100
four_num = (one_num // 10 % 10 + two_num // 10 % 10) % 10 * 10
five_num = (one_num % 10 + two_num % 10) % 10

print(three_num + four_num + five_num)
