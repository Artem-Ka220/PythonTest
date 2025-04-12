from math import trunc
from decimal import Decimal

yourNum = Decimal(input())
newNum = yourNum - trunc(yourNum)
print(newNum)
