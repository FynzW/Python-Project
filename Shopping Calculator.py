#Function to calculate the discounted price from the shopping item
def calculate_discount(price, discount_percent):
    return price * (discount_percent / 100)

#Function for the shopping summary including the items with the total of the price, discounted price and money saved
def print_summary(items, total_before, total_savings, budget):
    total_after = total_before - total_savings

    print("\n~Shopping Summary Lists~")
    for item in items:
        print(f"> {item['name']}: Original Price: ${item['price']:.2f} | Discount: {item['discount']}% | Final price: ${item['final_price']:.2f} | Money saved: ${item['savings']:.2f}")

    print("\n~Total Shopping Cost~")
    print(f"Total before discounts: ${total_before:.2f}")
    print(f"Total saved: ${total_savings:.2f}")
    print(f"Total after discounts: ${total_after:.2f}")

    if budget >= total_after:
        print(f"\nGood job! you are within your budget! You have saved ${budget - total_after:.2f} from your budget.")
    else:
        print(f"\nOh no! You have gone over budget by ${total_after - budget:.2f}.")
  
#Function to get the shopping budget of the user and making sure that the input was valid
def get_budget():

    print("Enter 'done' if you have finished your shopping lists.")

    budget_input = input("\nEnter your shopping budget: $")
    try:
        return float(budget_input)
    except ValueError:
        print("Invalid budget input. Setting budget to $0.")
        return 0

#The main with functions to be displayed, including loop item input with its price and discount
def main():
    items = []
    total_before = 0
    total_savings = 0

    print("\n~ Hi, Welcome to Shopping Counter! ~ ")

    budget = get_budget()

    while True:
        name = input("Enter item name: ")
        if name.lower() == 'done':
            break

        price_input = input(f"Enter price of {name}: $")
        try:
            price = float(price_input)
        except ValueError:
            print("That is not a valid price. Please enter a number.")
            continue
        
        while True:
            discount_input = input(f"Enter discount for {name} (%): ")
            try:
                discount = float(discount_input)
                if 0 <= discount <= 100:
                    break
                else:
                    print("Discount must be between 0% to 100%.")
            except ValueError:
                print("That is not a valid discount. Please enter a number.")
                continue

        savings = calculate_discount(price, discount)
        final_price = price - savings

        items.append({
            "name": name,
            "price": price,
            "discount": discount,
            "final_price": final_price,
            "savings": savings
        })

        total_before += price
        total_savings += savings

    print_summary(items, total_before, total_savings, budget)
    print("\n^Thank you for using this service! Hope to see you again!^")

main()
