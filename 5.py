price = int(input())

def sale(price):
    if price == 25:
        price += 3
    if price == 50:
        price += 8
    if price == 100:
        price += 20
    return price

print(sale(price))