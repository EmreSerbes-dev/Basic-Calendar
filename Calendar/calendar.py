import calendar

year = input("Which year do you want?")

if int(year) < 2000:
   print("Year error!!!!!")

month = input("Whick month do you want?")

if int(month) < 1 or int(month) > 12:
    print("Month error!!!!!")

print(calendar.month(int(year), int(month)))