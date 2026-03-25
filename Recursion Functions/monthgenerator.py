import calendar

def nex_month():
  count = 1
  while True:
    name = calendar.month_name[count]
    yield name
    count = count % 12 + 1

m = nex_month()
print(next(m))
print(next(m))
print(next(m))



# print(calendar.MONDAY)
# print(calendar.TUESDAY)
# print(calendar.SUNDAY)
# print(calendar.month_name[1])
# print(calendar.month_name[5])
# print(calendar.month_name[7])
# print(calendar.month_name[12])
# print(list(calendar.day_name))
# print(list(calendar.day_abbr))
# print(list(calendar.month_name))
# print(list(calendar.month_abbr))
# print(calendar.prmonth(2025,5))
# print(calendar.prmonth(2025,7))
# print(calendar.prmonth(2025,12))
# weeks  = calendar.monthcalendar(2026,1)
# print(weeks)
# cal  = calendar.TextCalendar()
# print(cal.pryear(2026))