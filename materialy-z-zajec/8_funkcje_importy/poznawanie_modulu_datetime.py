import datetime
now = datetime.datetime.now()
print(now)
print(now.strftime("%B"))
print(now.strftime("%B -> %A"))

rok_od_teraz = datetime.timedelta(days=365)

today = datetime.date.today()
print(today)
print(today + rok_od_teraz)

swieta = datetime.date(year=2021, month=12, day=24)
print(swieta)
do_swiat = swieta - today
print(do_swiat.days)

napis_z_data = "25-10-2021"
print(datetime.datetime.strptime(napis_z_data, "%d-%m-%Y"))