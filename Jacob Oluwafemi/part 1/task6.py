# prompt the user to input value of minutes and assign to a variable called minutes.
# divide minutes by 60 and assign it to a variable called hour.
# divide hour by 24 and assign it to variable called day.
#divide day by 365 and assign it to a variable called year.
#divide day by 365 using modulo to get the remainder and assign it to a variable called remaining days.



minutes = int(input("Enter minutes: ")) 

hour = minutes / 60
day = hour / 24
year = day // 365
remaining_days = day % 365
print(f'{year:.0f} years and {remaining_days:.0f} days')
