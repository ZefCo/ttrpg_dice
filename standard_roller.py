import init_dice
import dice_roller as dr
import re

def roller(d4=0, d6=0, d8=0, d10=0, d12=0, d20=0):
    
    standard_dice_file = 'standard_dice.json'

    standard_dice = init_dice.initialize_dice(standard_dice_file)

    standard_dice['d4'].set_ammount(d4)
    standard_dice['d6'].set_ammount(d6)
    standard_dice['d8'].set_ammount(d8)
    standard_dice['d10'].set_ammount(d10)
    standard_dice['d12'].set_ammount(d12)
    standard_dice['d20'].set_ammount(d20)

    roll = {k:v for k, v in standard_dice.items() if standard_dice[k].ammount > 0}

    results_array = {k:dr.random_generator(v.low, v.high, v.ammount) for k, v in roll.items()}

    return results_array

def cli():
    dice_hold = {'d4':0, 'd6':0, 'd8':0, 'd10':0, 'd12':0, 'd20':0}

    # print(dice_hold)

    print("input dice to roll")
    print("Input as d[#]=a1, d[#]=a2, d[#]=a3 : ")
    # dice = input('input dice: ')
    dice = 'd4=1, d6=10, d8=1'

    dice2roll = re.findall(r'd\d+=\d+', dice)
    
    for chunk in dice2roll:

        key = re.search(r'd\d+', chunk)
        key = key.group()
        
        ammount = re.search(r'=\d+', chunk)
        ammount = int(re.sub(r'=', '', ammount.group()))
        
        dice_hold[key] = ammount

    results = roller(d4=dice_hold['d4'],
                    d6=dice_hold['d6'],
                    d8=dice_hold['d8'],
                    d10=dice_hold['d10'],
                    d12=dice_hold['d12'],
                    d20=dice_hold['d20'])

    print(results)


def main():
    rolls = roller()
    print(rolls)

if __name__ in '__main__':
    main()