import init_dice
import dice_roller as dr
import re

def roller(b=0, s=0, a=0, d=0, p=0, c=0, f=0):
    
    starwars_dice_file = 'starwars_dice.json'

    starwars_dice = init_dice.initialize_dice(starwars_dice_file)

    starwars_dice['Boost'].set_ammount(b)
    starwars_dice['Setback'].set_ammount(s)
    starwars_dice['Ability'].set_ammount(a)
    starwars_dice['Difficulty'].set_ammount(d)
    starwars_dice['Proficency'].set_ammount(p)
    starwars_dice['Challenge'].set_ammount(c)
    starwars_dice['Force'].set_ammount(f)

    roll = {k:v for k, v in starwars_dice.items() if starwars_dice[k].ammount > 0}

    hold_array = {k:dr.random_generator(v.low, v.high, v.ammount) for k, v in roll.items()}

    # print(hold_array)

    # This generates an array of numbers: now to change that array of numbers to an array of results

    # print(starwars_dice['Boost'].r_array)
    # for thing in starwars_dice['Boost'].r_array:
    #     print(thing)

    results_array = {k:v for k, v in hold_array.items()}

    # return results_array

def cli():
    dice_hold = {'b':0, 's':0, 'a':0, 'd':0, 'p':0, 'c':0, 'f':0}

    # print(dice_hold)

    print("input dice to roll")
    print("Input as b=#, s=#, a=#, etc.")
    print("Only need first letter of the dice name")
    # dice = input('input dice: ')
    dice = 'b=1, f=10, p=1'

    dice2roll = re.findall(r'\w{1}=\d+', dice)
    
    for chunk in dice2roll:

        key = re.search(r'\w{1}', chunk)
        key = key.group()
        
        ammount = re.search(r'=\d+', chunk)
        ammount = int(re.sub(r'=', '', ammount.group()))
        
        dice_hold[key] = ammount

    results = roller(b=dice_hold['b'],
                    s=dice_hold['s'],
                    a=dice_hold['a'],
                    d=dice_hold['d'],
                    p=dice_hold['p'],
                    c=dice_hold['c'],
                    f=dice_hold['f'])

    print(results)

def main():
    results = {}
    pass

if __name__ in '__main__':
    main()