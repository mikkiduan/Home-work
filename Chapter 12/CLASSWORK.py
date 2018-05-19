import calendar
cal= calendar.TextCalendar(6)

cal.prmonth(2018,10)

d = calendar.LocaleTextCalendar(6, "klingon")
d.pryear(2012)

print(calendar.isleap(2022))

