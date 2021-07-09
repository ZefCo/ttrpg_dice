import random

def main():
    rand = random_generator(1, 10)
    print(rand, len(rand))

def random_generator(low, high, iterations=1):
    number_tup = []
    for _ in range(1, iterations + 1):
        rand = random.randint(low, high)
        number_tup.append(rand)
    number_tup = tuple(number_tup)
    return number_tup

if __name__ in '__main__':
    main()