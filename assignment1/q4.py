#Separates login hours into even-hour logins and odd-hour logins.
login_hours = [1, 3, 5, 7, 2, 6, 8, 4, 9, 10]
even_hours = []
odd_hours = []
for hour in login_hours:
    if hour % 2 == 0:
        even_hours.append(hour)
    else:
        odd_hours.append(hour)
print(even_hours)
print(odd_hours)

#Identifies login hours that fall into peak activity time (hours greater than 5).
login_hours = [1, 3, 5, 7, 2, 6, 8, 4, 9, 10]
peak_hours = []

for hour in login_hours:
    if hour > 5:
        peak_hours.append(hour)

print(peak_hours)

#Sorts the login hours in ascending order.
login_hours = [1, 3, 5, 7, 2, 6, 8, 4, 9, 10]

login_hours.sort()
print(login_hours)

#Calculates how many logins occurred during peak hours.
login_hours = [1, 3, 5, 7, 2, 6, 8, 4, 9, 10]
for hour in login_hours:
    if hour > 5:
        peak_hours.append(hour)
print(peak_hours)
print(len(peak_hours))

