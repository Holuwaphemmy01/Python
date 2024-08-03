employee_name = input('Enter your name: ')
hours_worked = float(input('Enter number of hours worked in a week: '))
hourly_pay_rate = float(input('Enter hourly pay rate: '))
gross_pay = hourly_pay_rate * hours_worked

federal_tax = 0.20 * gross_pay
state_tax = 0.09 * gross_pay
total_deduction = federal_tax + state_tax
net_pay = gross_pay - total_deduction


print(employee_name)
print(f'Hours worked: {hours_worked:.1f}')
print(f'Pay Rate: ${hourly_pay_rate}')
print(f'Gross Pay: ${gross_pay}')
print('Deductions: ')
print(f'Federal Withholding (20.0%): ${federal_tax}')
print(f'State Withholding (9.0%): ${state_tax:.2f}')
print(f'Net Pay: ${net_pay:.2f}')



 