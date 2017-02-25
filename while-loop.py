"""
This is a simple while loop
"""

x = 1

while x != 3:
    print ('x is ', x)
    x += 1

"""
This is a program for take a order in the restauran
"""
menu ={'Knackeredl': 0.5, 'Pip pip':1.5, 'Squidgy':2.5, 'Smashing':3.5}
orders=[]
order= input("what would you like to order?(Q to Quit)")

while (order.upper() != 'Q'):
    found = menu.get(order)
    if found:
        orders.append(order)
    else:
        print("Menu item doesn't exist")
    order= input ("Anything else? (Q to Quit)")

print(orders)

"""
This is other way that make, the program to take a order
"""

while True:
    order = input("Can i take your order? (Q to Quit)")
    if order == 'Cheeky Spam':
        print("Sorry, We're all out of that!")
        continue
    elif order.upper() == 'Q':
        break
    else:
            orders.append(order)
    pass
print (orders)
