slang = ['Knackeredl', 'Pip pip', 'Squidgy', 'Smashing']

menu =[]
"""
    In this part, the for loop, accross the list and concaten ' Spam' each word
    and save in the new list menu.
"""
for word in slang:
    menu.append(word + ' Spam' )
print (menu)

"""
now we create a dictionary with the list menu add the price, the price  is
one dolar expensive that the back product
"""
menu_price ={}
price = .5
for produc in menu:
    menu_price[produc]=price
    price = price + 1
print (menu_price)

"""
For print a dictionary (key and value) in diferent lines need a new for LOOP
you can see in next lines
"""
for name , price  in menu_price.items():
    print(name , ': $', format (price, '.2f'), sep='')

"""
note :
To get a list of the keys in a dictionary, use dict_ name.keys() and dict_name. value()
"""
