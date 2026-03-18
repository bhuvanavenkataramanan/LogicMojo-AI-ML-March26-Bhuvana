#Combines the product names and their prices into a single data structure representing a table.
products = ["Laptop","Phone","Tablet","Monitor","Headphones"]
amazon_prices = [75000, 45000, 30000, 20000, 5000]
flipkart_prices = [72000, 47000, 31000, 19500, 4800]

combined = []

for (product,amazon_price,flipkart_price) in zip(products,amazon_prices,flipkart_prices):
    combined.append([product,amazon_price,flipkart_price])
print(combined)

#Compares the price of each product across both platforms.
products = ["Laptop","Phone","Tablet","Monitor","Headphones"]
amazon_prices = [75000, 45000, 30000, 20000, 5000]
flipkart_prices = [72000, 47000, 31000, 19500, 4800]

combined = []

for (product,amazon_price,flipkart_price) in zip(products,amazon_prices,flipkart_prices):
    combined.append([product,amazon_price,flipkart_price])
print(combined)

print("product","amazon","flipkart")
for i in range(len(combined)):
    if combined[i][1] < combined[i][2]:
        print(combined[i][0],"lower","higher")
    elif combined[i][1] > combined[i][2]:
        print(combined[i][0],"higher","lower")
    else:
        print(combined[i][0],"same","same")

#Determines which platform offers the lower price.
products = ["Laptop","Phone","Tablet","Monitor","Headphones"]
amazon_prices = [75000, 45000, 30000, 20000, 5000]
flipkart_prices = [72000, 47000, 31000, 19500, 4800]

combined = []

for (product,amazon_price,flipkart_price) in zip(products,amazon_prices,flipkart_prices):
    combined.append([product,amazon_price,flipkart_price])
print(combined)

print("product","lowest-price","platform")
for i in range(len(combined)):
    if combined[i][1] <= combined[i][2]:
        print(combined[i][0],combined[i][1],"amazon")
    else:
        print(combined[i][0],combined[i][2],"flipcart")        

#Calculates the difference between the two prices.
products = ["Laptop","Phone","Tablet","Monitor","Headphones"]
amazon_prices = [75000, 45000, 30000, 20000, 5000]
flipkart_prices = [72000, 47000, 31000, 19500, 4800]

for (product,amazon_price,flipkart_price) in zip(products,amazon_prices,flipkart_prices):
    print(product,amazon_price-flipkart_price)

#Displays the product name, cheaper platform, and price difference.
products = ["Laptop","Phone","Tablet","Monitor","Headphones"]
amazon_prices = [75000, 45000, 30000, 20000, 5000]
flipkart_prices = [72000, 47000, 31000, 19500, 4800]

combined = []

for (product,amazon_price,flipkart_price) in zip(products,amazon_prices,flipkart_prices):
    combined.append([product,amazon_price,flipkart_price])
print(combined)

print("product","platform","price-difference")
for i in range(len(combined)):
    if combined[i][1] <= combined[i][2]:
        print(combined[i][0],"amazon",combined[i][2]-combined[i][1])
    else:
        print(combined[i][0],"flipcart",combined[i][1]-combined[i][2])