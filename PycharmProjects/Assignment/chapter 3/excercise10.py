principal_amount = 1000
annual_rate_return = 0.07
number_of_years = 30
amount_on_deposit = 0
counter = 0

for number in range (1, 31):
    counter += 1
    amount_on_deposit = principal_amount * (1 + annual_rate_return) ** counter
    print(f'The total amount for year {counter} is {amount_on_deposit} ')