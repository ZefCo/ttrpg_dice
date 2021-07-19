import random
import os
import dice_class as dc
import common_methods as cm
# import di

def random_generator(low, high, iterations):

    result_list = [random.randint(low, high) for _ in range(1, iterations + 1)]

    return result_list


def main():
    cwd = os.getcwd()
    standard_dice_path = os.path.join(cwd, 'JSONS', 'standard_dice.json')
    json = cm.load_json(standard_dice_path)
    standard_dice = {k:dc.Dice(k, v['low'], v['high'], v['results']) for (k, v) in json.items()}

    print(standard_dice)

    standard_dice['d4'].set_ammount(2)
    standard_dice['d6'].set_ammount(5)

    roll = {k:v for k, v in standard_dice.items() if standard_dice[k].ammount > 0}

    # print(roll)

    results = {k:random_generator(v.low, v.high, v.ammount) for k, v in roll.items()}
    print(results)

if __name__ in '__main__':
    main()