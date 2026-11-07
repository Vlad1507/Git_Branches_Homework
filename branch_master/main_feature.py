def calculate_discount(price, discount):
    return price - (price * discount / 100)


result = calculate_discount(1000, 15)
print(f"Final price: {result}")