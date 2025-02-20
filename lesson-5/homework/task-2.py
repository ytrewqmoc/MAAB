def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

principal = float(input("Enter the initial amount: "))
rate = float(input("Enter the annual rate of return (as a decimal): "))
years = int(input("Enter the number of years: "))

invest(principal, rate, years)