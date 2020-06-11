"""
Program : coupon_calculations.py
Author : Olivia Kennedy
Date Last Modified : 06/10/2020
This program is incomplete, but its goal is to accept input of price, cash coupon, and percent coupon and then
add the correct amount of shipping(5.95, 7.95, 11.95, or free) and tax.
"""
def calculate_price(price, cash_coupon, percent_coupon):
    TAX = 1.06
    subtotal = (price - cash_coupon) * (1 - percent_coupon)

    def shipping():
        if subtotal < 10:
            return 5.95
        else:
            return 7.95
        #not really sure how to get prices that arent 5.95 to work
        # i want the shipping for a subtotal less than 30 but greater than 10 to be 7.95
        # i want the shipping for a subtotal less than 50 but greater than 30 to be 11.95
        # i want the shipping for a subtotal greater than 50 to be free


    price_with_shipping = subtotal + shipping()
    final_price = round((price_with_shipping * TAX), 2)
    return final_price

if __name__ == '__main__':
    price = float(input("How much is this purchase:"))
    cash_coupon = float(input("Do you have a cash off coupon, if so is it worth 5 or 10 dollars:"))
    percent_coupon = float(input("Enter the amount of your percent off discount as its decimal. (If you have 20% off you would answer '.20' "))
    print("Your order costs", calculate_price, "dollars")
