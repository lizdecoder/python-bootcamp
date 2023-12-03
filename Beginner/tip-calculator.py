# Python-bootcamp: 100 days of code 
# Day 2

print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
tip_percent = float(input('What percent tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

tip = tip_percent/100
payment = (bill / people) * (1.00 + tip)

format_payment = "{:.2f}".format(payment)

print(f'Each person should pay: ${format_payment}')