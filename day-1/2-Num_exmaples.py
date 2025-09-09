##_float methods_##


float_a=5.0
float_b=2.5


print(float_a+ float_b)
print(float_a-float_b)
print(float_a/float_b)
print(float_a // float_b)
print(float_a*float_b)
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5) #3.14


# Integer variables
num1 = 10
num2 = 5

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)

# power
print(pow(2, 3))   # 8
print(2 ** 3)      # 8 (same as pow)

# max min
print(min(10, 5, 20))   # 5
print(max(10, 5, 20))   # 20

# type con

print(float(5))     # 5.0
print(int(5.9))     # 5
print(str(5.9))     # '5.9'



import math

print(math.ceil(4.2))   # 5
print(math.floor(4.9))  # 4
print(math.sqrt(16))    # 4.0
print(math.log(100, 10))# 2.0

import random

print(random.random())         # Random float between 0 and 1
print(random.randint(1, 100))  # Random int between 1 and 100


















# You don’t need heavy math like data science. Just:

# Basic operators (+ - * / // %)

# round(), abs(), min(), max(), divmod()

# Type conversion (int(), float(), str())

# math.ceil(), math.floor() (sometimes)

# Maybe random for testing
