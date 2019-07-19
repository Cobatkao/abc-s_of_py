#!/usr/bin/env python3
msg = "Hello World"
print(msg)

# 获得月份数和天数
# *divmod会执行：两项先相除，再取余数，组成tuple，再用*拆分元祖
days = int(input("Enter days..."))
m = "Month {} and Days {}".format(*divmod(days, 30))
print(m)
print()

# 斐波那契0-100
a, b = 0, 1
while b < 100:
  print(b, end=" ")
  a, b = b, a + b
# 1 1 2 3 5 8 13 21 34 55 89

print()

# 99乘法表
i = 1
print('*' * 75)
while i < 11:
  j = 1
  while j < 11:
    print("{:5d}".format(i * j), end=' ')
    j += 1
  print()
  i += 1
print('*' * 75)
# ***************************************************************************
#     1     2     3     4     5     6     7     8     9    10
#     2     4     6     8    10    12    14    16    18    20
#     3     6     9    12    15    18    21    24    27    30
#     4     8    12    16    20    24    28    32    36    40
#     5    10    15    20    25    30    35    40    45    50
#     6    12    18    24    30    36    42    48    54    60
#     7    14    21    28    35    42    49    56    63    70
#     8    16    24    32    40    48    56    64    72    80
#     9    18    27    36    45    54    63    72    81    90
#    10    20    30    40    50    60    70    80    90   100 
# ***************************************************************************

# 打星号1
t = int(input("Enter the number of rows: "))
while t >= 0:
  print("*" * t)
  t -= 1
# *****
# ****
# ***
# **
# *

# 打星号2
t = int(input("Enter the number of rows: "))
q = t
while t >= 0:
  plus = "*" * t
  divide = " " * (q - t)
  print(divide + plus)
  t -= 1
# *****
#  ****
#   ***
#    **
#     *

# 打星号3
t = int(input("Enter the number of rows: "))
i = 1
while i <= t:
  print("*" * i)
  i += 1
# *
# **
# ***
# ****
# *****

# 棍子游戏
# 有 21 根棍子，首先用户选 1 到 4 根棍子，然后电脑选 1到 4 根棍子。谁选到最后一根棍子谁就输
# PS. 用户和电脑一次选的棍子总数只能是5。
sticks = 21
while 1 == 1:
  print("sticks left: ", sticks)
  stick_taken = int(input("How many sticks do you wanna take? "))
  if (sticks == 1):
    print("you loose!")
    break
  if (stick_taken > 5):
    print("You are only allowed to take 1~4 sticks!")
    continue
  print("Computer took {} sticks".format(5 - stick_taken))
  sticks -= 5
