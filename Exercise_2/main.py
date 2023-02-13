"""Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел."""


import sys


def recursion_sum(number_a, number_b):
    """The method finds sum of numbers using recursion"""
    if number_a == 0:
        return number_b
    return recursion_sum(number_a - 1, number_b + 1)


def testing_recursion_sum(test_num=3, test_pow=2):
    """The method tests recursion_sum method"""
    print("Testing of the \"recursion_sum\" method has been launched...")
    expected = 5
    actual = recursion_sum(test_num, test_pow)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_recursion_sum()
print()


try:
    num_a = int(input("Enter your number \"a\": "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


try:
    num_b = int(input("Enter your number \"b\": "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


print()
RESULT = recursion_sum(num_a, num_b)
print(f"{num_a} plus {num_b} is {RESULT}")
