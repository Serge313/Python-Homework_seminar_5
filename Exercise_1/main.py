"""Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии."""


import sys


def recursion_pow(number, power_to_raise):
    """The method raises number to power using recursion"""
    if power_to_raise == 0:
        return 1
    if power_to_raise == 1:
        return number
    return number * recursion_pow(number, power_to_raise - 1)


def testing_recursion_pow(test_num=3, test_pow=5):
    """The method tests recursion_pow method"""
    print("Testing of the \"recursion_pow\" method has been launched...")
    expected = 243
    actual = recursion_pow(test_num, test_pow)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_recursion_pow()
print()


try:
    num = int(input("Enter your number: "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


try:
    power = int(input("Enter the power in which you want to raise the number: "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


print()
RESULT = recursion_pow(num, power)
print(f"Number {num} to the power {power} is {RESULT}")
