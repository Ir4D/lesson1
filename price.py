def format_price(price):
    price = int(price)
    price = str(price)
    return 'Цена: ' + price + ' руб.'

p = format_price(56.24)
print(p)