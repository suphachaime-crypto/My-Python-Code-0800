prices = []

for i in range(6):
    price = int(input(f"Item {i+1}: "))
    prices.append(price)
 
budget = int(input("Enter total budget: "))
 
total = 0
bought = []
 
print("\n--- Result ---")

for i in range(6):
    if total + prices[i] <= budget:
        print(f"Item {i+1} = {prices[i]} -> buy")
        total += prices[i]
        bought.append(prices[i])
        print(f"Current total = {total}")
    else:
        print(f"Item {i+1} = {prices[i]} -> cannot buy")
 
print("\n--- Summary ---")
print(f"Bought items: {bought}")
print(f"Total spent: {total}")
print(f"Remaining budget: {budget - total}")