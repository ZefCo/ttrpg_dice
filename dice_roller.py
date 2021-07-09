import random
import file_importer as fi
import os
import dice_class as dc

def random_generator(low, high, iterations=1):
    number_tup = []
    for _ in range(1, iterations + 1):
        rand = random.randint(low, high)
        number_tup.append(rand)
    number_tup = tuple(number_tup)
    return number_tup


def handful_of_dice(*args, **kwargs):
    # pass
    # for thing in args:
    #     print(thing)
    for dice, count in kwargs.items():
        if dice in args.keys():
            print(dice)
        # print(dice, count)
    # results_tup = list
    # print(d4)
    #     results = random_generator(1, dice, iterations=count)
    #     results_tup.append(results)
    # results_tup = [output for output in random_generator(1, kwargs.keys(), iterations=kwargs.values())]
    # results_tup = tuple(results_tup)
    # return results_tup

def main():
    pass
    # test = temp_importer()
    # handful_of_dice()
    # print(test['d4'].name, type(test['d4'].name))
    # print(test, type(test))
    # name_hold(test['d4'].name=1)

    # print(j.json_data)
    # rand = random_generator(1, 10)
    # print(rand, len(rand))
    # name_hold(10=1, 8=1)

if __name__ in '__main__':
    main()