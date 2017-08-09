import sys, getopt
from csv import writer
from math import floor

def main(argv):
	## initialization ##
	# initialize argument variables
	initialDebt = 0
	interestRate = 0
	payment = 0

	# initialize getopt (credit: https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
	try: 
		options, arguments = getopt.getopt(argv, "hd:i:p", ["debt=", "interest=", "payment="])
	except getopt.GetoptError:
		print 'paymentCalculator.py -d <initial debt> -i <interest rate> -p <payment amount>'
		sys.exit(2)
	for option, argument in options:
		if opt == '-h':
			print 'paymentCalculator.py -d <initial debt> -i <interest rate> -p <payment amount>'
			sys.exit(2)
		elif option in ("-d", "--debt"):
			initialDebt = argument
		elif option in ("-i", "--interest"):
			interestRate = argument
		elif option in ("-p", "--payment"):
			payment = argument

	# constants
	daysBetweenPayments = 15
	daysPerYear = 365

	# initialized variables
	interestToPay = 0
	principleReduced = 0
	paymentNumber = 1
	debtRemainingAfterPayment = initialDebt
	debtRemainingBeforePayment = initialDebt
	interestRatePer15DayCycle = (interestRate / daysPerYear) * daysBetweenPayments

	## debt calculation ##
	# open file
	writer = csv.writer(open('paymentRecord.csv', 'w', newline = ''))

	# add column headers
	writer.writerow(['Payment Number', 'Debt Remaining Before Payment', 'Interest to be Paid', 'Payment', 'Principle Reduced', 'Debt Remaining After Payment'])

	# iterate until debt is repayed
	while debtRemainingAfterPayment > 0:
		debtRemainingBeforePayment = debtRemainingAfterPayment
		interestToPay = debtRemainingBeforePayment * interestRatePer15DayCycle
		principleReduced = payment - interestToPay
		debtRemainingAfterPayment = debtRemainingBeforePayment - principleReduced
		writer.writerow([paymentNumber, debtRemainingBeforePayment, interestToPay, payment, principleReduced, debtRemainingAfterPayment])
		writer.writerow([''])
		paymentNumber = paymentNumber + 1

	# calculate metrics about repayment and add to final row
	totalDays = paymentNumber * daysBetweenPayments
	totalMonths = floor(totalDays/30.4)
	totalYears = totalMonths/12
	writer.writerow(['Total payments:', paymentNumber, 'Days in repayment:', totalDays, 'Months in repayment:', totalMonths, 'Years in repayment:', totalYears])

if __name__ == "__main__":
   main(sys.argv[1:])
