def calculate_ticket_price(age, day, is_group):

    adult_price = 12
    child_price = 8
    senior_price = 10

    if is_group:
        adult_price *= 0.9
        child_price *= 0.8
        senior_price *= 0.85

    if age >= 18:
        ticket_price = adult_price
    elif 13 <= age <= 17:
        ticket_price = child_price
    else:
        ticket_price = senior_price

    if day in ['saturday', 'sunday']:
        ticket_price *= 0.2 
    return ticket_price

age = int(input("Enter age: "))
day_of_week = input("Enter day of the week: ")

is_group = input("Are you part of a group? (yes/no) ") == 'yes'

ticket_price = calculate_ticket_price(age, day_of_week, is_group)
print(f"Your ticket price is: ${ticket_price}")
