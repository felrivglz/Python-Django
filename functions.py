def avarage(numbers):
    total = 0
    for num in numbers:
        total =total + num

    avg = total/len(numbers)
    return avg

def main():
   prices = [2.5, 3, 4.50, 5]
   result = avarage(prices)
   print(result)

main()
