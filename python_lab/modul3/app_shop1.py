shop1 = {'apples': 7.5, 'plums': 8.3, 'bread': 3.5}
shop2 = {'apples': 7.6, 'plums': 8.1, 'bread': 3.5}
shop3 = {'apples': 7.4, 'plums': 8.9, 'bread': 3.5}
shopping_cart = {'apples': 3, 'plums': 5, 'bread': 4}
shops = {'lidl': shop1, 'kauf': shop2, 'profi': shop3}
result = {}
# what is the cheapest shop

for shop_name, shop in shops.items():
    for product, quantity in shopping_cart.items():
        if result.get(shop_name):  # pt toate produsele
            result.update({shop_name: (shop[product] * quantity) + result[shop_name]})
        else:
            result.update({shop_name: shop[product] * quantity})
print(result)

for result in shopping_cart.items():
    print(str(shop_name) + ' este cel mai ieftin magazin')
