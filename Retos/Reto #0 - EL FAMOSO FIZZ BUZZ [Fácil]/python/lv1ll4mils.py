
def fizzbuzz():

    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzfuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("fuzz")
        else:
            print(f"{number}")

fizzbuzz()