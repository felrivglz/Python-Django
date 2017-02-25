"""
in this program we see how open a txt file and writing, reading and append
"""
def first():
    sales_log = open('spam_ordes.txt', 'w')
    """
        'w' for write
        'r' for read
        'a' for append

        in the next lines write in the txt file called spam_ordes.txt
    """

    sales_log.write('The spam van\n')
    sales_log.write('Sales log')

    """
    finaly close the txt file
    """
    sales_log.close()

def write_sales_log(order):
    file= open('sales.txt', 'a')
    file.write('\n')
    total = 0
    for key, value  in order.items():
        file.write(key + ' ' + format(value, '.2f') + '\n')
        total += value
    file.write('total is:' + format(total, '.2f') +'\n' )
    file.close()

def main():
    order= {'Cheeky': 1.0, 'Smashing': 2.5, 'Cheerio':3.0, 'Cheeky': 1.0, 'Smashing': 2.0,}
    write_sales_log(order)
    order= {'Cheeky': 1.0, 'Smashing': 2.0, 'Cheerio':3.6}
    write_sales_log(order)
    order= {'Cheeky': 1.0, 'Smashing': 2.4, }
    write_sales_log(order)

main()
