#!/usr/bin/env python3
"""Simple command line python script that outputs a spreadsheet of data about your debt payments. Jorin Weatherston August, 2017"""
import csv
import sys, getopt
from math import floor

def main(argv):
    ## initialization ##
    # initialize argument variables
    initial_debt = 0
    interest_rate = 0
    payment = 0

    # initialize getopt (credit: https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
    try:
        options, arguments = getopt.getopt(argv, "hd:i:p", ["debt=", "interest=", "payment="])
    except getopt.GetoptError:
        print('Error: Accepted format is: ./debt_calculator.py -d <initial debt> -i <interest rate> -p <payment amount>')
        sys.exit(2)
    for option, argument in options:
        if option == '-h':
            print('./debt_calculator.py -d <initial debt> -i <interest rate> -p <payment amount>')
            sys.exit(2)
        elif option in ('-d', "--debt"):
            initial_debt = float(argument)
        elif option in ('-i', "--interest"):
            interest_rate = float(argument)
        elif option in ('-p', "--payment"):
            payment = float(argument)

    # constants
    days_between_payments = 15
    days_per_year = 365

    # initialized variables
    interest_to_pay = 0
    principle_reduced = 0
    payment_number = 1
    debt_remaining_after_payment = initial_debt
    debt_remaining_before_payment = initial_debt
    interest_rate_per_15_day_cycle = (interest_rate / days_per_year) * days_between_payments

    ## debt calculation ##
    # open file
    writer = csv.writer(open('paymentRecord.csv', 'w', newline=''))

    # add column headers
    writer.writerow(['Payment Number', 'Debt Remaining Before Payment', 'Interest to be Paid', 'Payment', 'Principle Reduced', 'Debt Remaining After Payment'])

    # iterate until debt is repayed
    while debt_remaining_after_payment > 0:
        debt_remaining_before_payment = debt_remaining_after_payment
        interest_to_pay = debt_remaining_before_payment * interest_rate_per_15_day_cycle
        principle_reduced = payment - interest_to_pay
        debt_remaining_after_payment = debt_remaining_before_payment - principle_reduced
        writer.writerow([payment_number, debt_remaining_before_payment, interest_to_pay, payment, principle_reduced, debt_remaining_after_payment])
        writer.writerow([''])
        payment_number = payment_number + 1

    # calculate metrics about repayment and add to final row
    total_days = payment_number * days_between_payments
    total_months = floor(total_days/30.4)
    total_years = total_months/12
    writer.writerow(['Total payments:', payment_number, 'Days in repayment:', total_days, 'Months in repayment:', total_months, 'Years in repayment:', total_years])
    print('Success.')
    print('Total payments:', payment_number, ', Days in repayment:', total_days, ', Months in repayment:', total_months, ', Years in repayment:', total_years)
    print('Goodluck with your payments!')

if __name__ == "__main__":
    main(sys.argv[1:])
