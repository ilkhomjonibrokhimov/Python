def invest(amount, rate, years):
    for year in range(1, years+1):
        amount += amount*(rate)
        print(f"Year {year}: ${amount:.2f}")

  
amount = int(input("The amount you want to invest $: "))
rate = float(input("The rate you want to get: "))
years = int(input("How many year do you want to invest for: "))

invest(amount, rate, years)


