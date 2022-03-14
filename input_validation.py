"""
Program: input_validation.py
Author: Jessie Horvath
Last date modified: 02/06/2022

The purpose of this program is to validate and accept input from a user 
for first and last name, age, and three test scores. 
"""

from logging import exception


first_name = input("What is your first name? ")
last_name = input("And your last name? ")
age = input("How old are you? ")

try:
    first_score = input("Enter your first test score: ")
    first_score_int = int(first_score)
    if 100 >= first_score_int >= 0:
        print("Input is good.")
    else:
        raise ValueError("Bad Input")
    second_score = input("Enter your second test score: ")
    second_score_int = int(second_score)
    if 100 >= second_score_int >= 0:
        print("Input is good.")
    else:
        raise ValueError("Bad Input")
    third_score = input("Enter your third test score: ")
    third_score_int = int(third_score)
    if 100 >= third_score_int >= 0:
        print("Input is good.")
    else:
        raise ValueError("Bad Input")
    average_score = (first_score_int + second_score_int + third_score_int) / 3
    print(f"{last_name}, {first_name} age: {age} average grade: {average_score:5.2f}")
except Exception as error:
    print(repr(error))
