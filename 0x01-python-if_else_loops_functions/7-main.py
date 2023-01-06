#!/usr/bin/python3
islower = __import__('7-islower').islower

print("a is {}". format("islower" if islower("a") else "Upper"))
print("H is {}". format("islower" if islower("H") else "Upper"))
print("A is {}". format("islower" if islower("A") else "Upper"))
print("3 is {}". format("islower" if islower("3") else "Upper"))
print("g is {}". format("islower" if islower("g") else "Upper"))
