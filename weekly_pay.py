"""
Program: weekly_pay.py
Author: Jessie Horvath
Last date modified: 02/06/2022

This function asks for an employee's name, hours worked, and hourly rate of pay.
It calculates the weekly pay using the hours worked and hourly rate of pay inputs as
parameters. The end result returns a string of their name and weekly pay.
"""


def weekly_pay(hours, pay):
    calculated_weekly_pay = hours * pay
    return calculated_weekly_pay


if __name__ == '__main__':
    try:
        name = input("Enter your name: ")
        hours_worked = int(input("Enter the number of hours worked: "))
        pay_rate = float(input("Enter your pay rate: "))
    except ValueError as error:
        print("ValueError found!")
    else:
        print("Name: " + name + ", Weekly Pay: " +
              str(weekly_pay(hours_worked, pay_rate)))
