#Design a function that takes the ordered items, quantities, and prices to calculate the total bill amount.
#Include options for applying discounts, taxes, and splitting the bill among friends.

def calculate_total_amount(quantities, prices,applying_discount, taxes, splitting_bill):

    if applying_discount:
        prices *= 0.9
    else:
        print("no discount")

    if splitting_bill:
        prices /= 2
    return prices*quantities+taxes

        

taxes = 0.01
quantities = int(input("Enter Quantities? "))
prices = int(input("Enter the Prices? "))
applying_discount = (input("want to apply Discounts Yes/No? ")) == 'yes'
splitting_bill = input("split the bill Yes/No? ") == "yes"
total_bill = calculate_total_amount(quantities, prices, applying_discount, taxes, splitting_bill )
if splitting_bill == True:
    print("Your Total Bill perperson is " ,{total_bill})
else:
    print("Your Total Bill is " ,{total_bill})
