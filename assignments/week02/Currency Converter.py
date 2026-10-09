print("Currency Converter")
print("1. THB to USD")
print("2. USD to THB")

choice = input("Choose conversion direction (1 or 2): ")
amount = float(input("Enter amount to convert: "))

exchange_rate = 35.5

if choice == "1":
    result = amount / exchange_rate
    print(f"Formula: USD = THB / {exchange_rate}")
    print(f"Result: {result:.2f} USD")

elif choice == "2":
    result = amount * exchange_rate
    print(f"Formula: THB = USD * {exchange_rate}")
    print(f"Result: {result:.2f} THB")

else:
    print("Invalid choice. Please choose 1 or 2.")