import random
"""
    'range(10)' generate a list of [0, ..., (10-1)]
    range(10) = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
for i in range(10):
    ticket = random.randint(1,100)
    print(ticket)
"""
    'range(2005, 2016, 2) generate a list of [2005, ..., 2016] eache 2 year
    range(2005, 2016, 2) = [2005, 2007, 2009, 2011, 2013, 2015]
"""

for i in range(2005, 2016, 2):
    print (i)
