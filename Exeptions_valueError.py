"""
    Python has 60-plus types of exceptions in the next list show the most
    used:

        FileNotFoundError  File doesn't exist
        IndexError         Index out of bounds
        KeyError           key doesn't exist
        NameError          variable name doesn't exist in local o globar scope
        ValueError         Value is the wrong types
"""
price = input("Enter the price")
try:
    price = float(price)
    print('Price=', price)
except ValueError as err:
    print('THIS IS A ERROR \n',err)
