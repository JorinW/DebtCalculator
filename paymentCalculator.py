import csv
from math import floor
initalDebt = 90885
interestRate = 0.027
daysBetweenPayments = 15
daysPerYear = 365
payment = 750
paymentNumber = 1
interestToPay = 0
principleReduced = 0
debtRemainingAfterPayment = 90885
debtRemainingBeforePayment = 90885
interestRatePer15DayCycle = (interestRate / 365) * 15

writer = csv.writer(open('paymentRecord.csv', 'w', newline = ''))
writer.writerow(['Payment Number', 'Debt Remaining Before Payment', 'Interest to be Paid', 'Payment', 'Principle Reduced', 'Debt Remaining After Payment'])
while debtRemainingAfterPayment > 0:
	debtRemainingBeforePayment = debtRemainingAfterPayment
	interestToPay = debtRemainingBeforePayment * interestRatePer15DayCycle
	principleReduced = payment - interestToPay
	debtRemainingAfterPayment = debtRemainingBeforePayment - principleReduced
	writer.writerow([paymentNumber, debtRemainingBeforePayment, interestToPay, payment, principleReduced, debtRemainingAfterPayment])
	writer.writerow([''])
	paymentNumber = paymentNumber + 1


totalDays = paymentNumber * daysBetweenPayments
totalMonths = floor(totalDays/30.4)
totalYears = totalMonths/12
writer.writerow(['Total payments:', paymentNumber, 'Days in repayment:', totalDays, 'Months in repayment:', totalMonths, 'Years in repayment:', totalYears])
