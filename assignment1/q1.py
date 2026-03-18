
transactions = [1200, 3000, 250, 7800, 540, 3000, 9100, 250, 1500, 7800]

#Identify and display all transaction values that appear more than once.
num_list = []
for value in transactions:
    if transactions.count(value) > 1:
        if value not in num_list:
            num_list.append(value)
print(num_list)

#Detect transactions greater than ₹5000 as these may require fraud monitoring.

for value in transactions:
    if value > 5000:
        print(value)

#Create a new list containing only unique transaction values.

unique = []
for value in transactions:
    if transactions.count(value) == 1:
            unique.append(value)
print(unique)

#Calculate the total spending for the day.

total = 0
for value in transactions:
    total = total + value

print(total)

#Sort the unique transaction list in descending order to view the largest transactions first.

unique = []
for value in transactions:
    if transactions.count(value) == 1:
            unique.append(value)
unique.sort(reverse=True)
print(unique)
