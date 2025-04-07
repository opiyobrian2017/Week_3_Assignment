# creating function to calculate discount
# This function takes the original price and discount percentage as inputs and returns the final price after applying the discount if applicable.
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: ${final_price}")
    else:
        print(f"No discount applied. The original price is: ${original_price}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")