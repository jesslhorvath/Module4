"""
Program: hourly_employee_input.py
Author: Jessie Horvath
Last date modified: 02/06/2022

The purpose of this program is to create a function that prompts
a user for their name, hours worked, and hourly pay rate and then
to return that information in a string while handling bad input.
"""


def hourly_employee_input():
    try:
        name = input("Enter your name: ")

        hours_worked = input("Enter amount of hours worked: ")
        hours_worked_int = int(hours_worked)
        if hours_worked_int < 0:
            raise ValueError("No negative numbers please")

        pay_rate = input("Enter hourly rate of pay: ")
        pay_rate_float = float(pay_rate)
        if pay_rate_float < 0:
            raise ValueError("No negative numbers please")

        print(
            f"Name: {name}, Hours worked: {hours_worked_int}, Hourly Pay Rate: ${pay_rate_float:.2f}")
        print(
            f"So, {name}, you made ${hours_worked_int * pay_rate_float:.2f} this week, nice.")
    except Exception as error:
        print(repr(error))


hourly_employee_input()
