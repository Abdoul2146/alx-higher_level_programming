#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
if n > 5:
    print(f"the last digit of {number} is {n} and is greater than 5")
elif n == 0:
    print(f"the last digit of {number} is {n} and is is 0")
elif n < 6 and not 0:
    print(f"the last digit of {number} is {n} and is less than 6 and not 0")
