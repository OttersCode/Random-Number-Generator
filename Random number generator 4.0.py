import random
import os
def main():
    os.system("title Random Number Generator 4.0")
    lower=input("Lowest number?:")
    highest=input("Highest number?:")
    quantity = input("Qauntity:")
    lower=int(lower)
    highest=int(highest)
    quantity=int(quantity)
    n = 0
    while n!=quantity:
        print(random.randint(lower,highest))
        n += quantity
    if n==quantity:
        input("Press Enter")
        os,system("cls")
        main()

main()

