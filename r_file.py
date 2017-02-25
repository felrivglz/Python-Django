def read_dollar_menu():
    """
        Python has 60-plus types of exceptions in the next list show the most
        used:

            FileNotFoundError  File doesn't exist
            IndexError         Index out of bounds
            KeyError           key doesn't exist
            NameError          variable name doesn't exist in local o globar scope
            ValueError         Value is the wrong types
    """
    try:
        dollar_spam= open('dollar_spam.txt', 'r')
        dollar_menu= []
        for line in dollar_spam:
            """
                strip use for delete special carateres like \n or \t
            """
            line = line.strip()
            dollar_menu.append(line)

        print(dollar_menu)
        dollar_spam.close()
    except:
        print("File don't exist")

def main():
    read_dollar_menu()

main()
