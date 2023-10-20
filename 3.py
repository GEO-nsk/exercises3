price = int(input())
card = str(input('У вас есть карта?'))
holiday = str(input('Сейчас праздник?'))

if card == 'да':
    card = True
if card == 'нет':
    card = False

if holiday == 'да':
    holiday = True
if holiday == 'нет':
    holiday = False

def sale(price,card,holiday):
    sale_number = 0

    if price > 5000 and price <= 15000:
        sale_number += 3
    if price > 15000 and price <= 20000:
        sale_number += 5
    if price > 20000 and price <= 30000:
        sale_number += 7
    if price > 30000:
        sale_number += 10
    if card:
        sale_number += 5
    if holiday:
        sale_number += 3
    if sale_number > 15:
        sale_number = 15

    price = price * (1 - (sale_number/100))
    return price

print(round(sale(price,card,holiday),2))