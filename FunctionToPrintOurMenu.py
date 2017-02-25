
def print_menu(menu):
    for name, price in menu.items():
        print(name, ':$', format(price, '.2f'), sep='')

def get_order(menu):
    orders=[]
    order= input("what would you like to order?(Q to Quit)")

    while (order.upper() != 'Q'):
        found = menu.get(order)
        if found:
            orders.append(order)
        else:
            print("Menu item doesn't exist")
        order= input ("Anything else? (Q to Quit)")
    return orders

def bill_total(orders, menu):
    total = 0
    for order in orders:
        total += menu[order]
    return total

def main():
    menu ={'Knackeredl': 0.5, 'Pip pip':1.5, 'Squidgy':2.5, 'Smashing':3.5}
    print_menu(menu)
    orders=get_order(menu)
    total = bill_total(orders, menu)
    print("your orden", orders,
          "your total is:$", format(total,'.2f'), sep='')


main()
