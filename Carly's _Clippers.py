hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# point 1
total_price =0
# point 2
for price in prices:
  total_price += price
# point 3
average_price = total_price/len(prices)
# point 4
print(f"Average Haircut Price: {average_price}")
# point 5
new_prices = [price -5 for price in prices]
# point 6
print(new_prices)
# point 7
total_revenue = 0
# point 8 
for i in range(len(hairstyles)):
# point 9 
  total_revenue += prices[i] * last_week[i]
# point 10
print(f"Total Revenue: {total_revenue}")
# point 11
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)
# point 12
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)-1) if new_prices[i]<30]
# point 13
print(cuts_under_30)