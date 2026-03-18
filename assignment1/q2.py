
#Iterates through the dataset and removes all invalid age values.
ages = [25, 42, -1, 34, None, 52, 17, -5, 29, None, 46]
for age in ages:
    if age is None or age < 0:
        ages.remove(age)
print(ages)

#Stores only valid ages in a new list.
ages = [25, 42, -1, 34, None, 52, 17, -5, 29, None, 46]
new_ages = []
for age in ages:
    if age is not None and age > 0:
        new_ages.append(age)
print(new_ages)

#Calculates the average age of valid customers.
ages = [25, 42, -1, 34, None, 52, 17, -5, 29, None, 46]
new_ages = []
for age in ages:
    if age is not None and age > 0:
        new_ages.append(age)
print(new_ages)
sum = 0
for age in new_ages:
    sum = sum + age
avg_age = sum/len(new_ages)
print(avg_age)

#Displays the list of customers whose age is greater than 30.
ages = [25, 42, -1, 34, None, 52, 17, -5, 29, None, 46]
for index,age in enumerate(ages):
    if age is not None and age > 30:
        print(index,age)

#Prints how many invalid entries were removed during the cleaning process.
ages = [25, 42, -1, 34, None, 52, 17, -5, 29, None, 46]
invalid = 0
for age in ages:
    if age is None or age < 0:
        ages.remove(age)
        invalid = invalid + 1
print(ages)
print(invalid)