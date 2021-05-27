import  calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2021, 8))
print()

print(calendar.calendar(2021))

day_of_the_week_=calendar.weekday(2021, 9, 9)
print(day_of_the_week_)

is_leap=calendar.isleap(2021)
print(is_leap)

how_many_leap_days= calendar.leapdays(2000, 2021)
print(how_many_leap_days)