def calculate_price(price, cash_coupon, percent_coupon):
    TAX = 1.06
    subtotal = (price - cash_coupon) * (1 - percent_coupon)
    if subtotal < 10:
        price_with_shipping = subtotal + 5.95
    final_price = round((price_with_shipping * TAX), 2)
    return final_price

if __name__ == '__main__':
    price = float(input("How much is this purchase:"))
    cash_coupon = float(input("Do you have a cash off coupon, if so is it worth 5 or 10 dollars"))
    percent_coupon = float(input("Enter the amount of your percent off discount as its decimal. (If you have 20% off you would answer '.20' "))
    print("Your order costs", calculate_price, "dollars")

