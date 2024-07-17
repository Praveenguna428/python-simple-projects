def calculate_ticket_price (age, movie_type):
    if age<= 5:
        return 100.00
    elif age <= 18:
        return 120.00
    else:
        base_price = 120.00
    if movie_type == "3D":
        base_price += 20.00
    return base_price

age = int (input("Enter the age:"))
movie_type = input("Enter the Movie type (Regular/3D):")
ticket_price = calculate_ticket_price (age, movie_type)
print("Ticket price:${:.2f}".format(ticket_price))

