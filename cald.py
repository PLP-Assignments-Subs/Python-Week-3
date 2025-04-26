def calculate_discount(price, discount):
    if discount_percent >= 20:
        discount_amount = price * (discount / 100)
        final_price = price - discount_amount
        return final_price
    else: 
        return price
    
# Getting users input
try:
    original_price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)

    if discount_percent >= 20:
        print(f"The final price after a discount of {discount_percent}% is: {final_price:.2f}")
    else:
        print(f"The price is: {original_price:.2f} (No discount applied)")

except ValueError:	
    print("Please enter valid numbers for price and discount percentage.")

loop = True
while loop:
    try:
        original_price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(original_price, discount_percent)

        if discount_percent >= 20:
            print(f"The final price after a discount of {discount_percent}% is: {final_price:.2f}")
        else:
            print(f"The price is: {original_price:.2f} (No discount applied)")

        # Here you ask if the user wants to continue
        choice = input("Do you want to calculate another discount? (yes/no): ").strip().lower()
        if choice != 'yes':
            loop = False
            print("Thank you for using the discount calculator. Goodbye!")

    except ValueError:
        print("Please enter valid numbers for price and discount percentage.")