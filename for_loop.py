prices = [2.5, 3.5, 4.5]
"""
'price' is a temporary vaariable that holds
one of the 'prices' in the list for eache run
"""
total=0
for price in prices :
    print('Price is', price)
    """
    In python 2.7 'print 'Price is', price'.
    because in the:
        TIME IN THE LOOP   price      output
        frist              2.5        Price is 2.5
        second             3.5        Price is 3.5
        third              4.5        Price is 4.5
    """
    total=total + price
    print ('Total is:', total)

average= total/len(prices)
print ('avg is', average)
