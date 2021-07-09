import dice_roller as dr
import dice_class as dc
import file_importer as fi
import dice_bag as db
import os

def main():
    # pass
    cwd = os.getcwd()
    standard_dice_path = os.path.join(cwd, 'JSONS', 'standard_dice.json')
    dice_bag = db.grab_dice(standard_dice_path)
    # print(dice_bag, type(dice_bag))
    dr.handful_of_dice(dice_bag, d4=1, d6=2)

if __name__ in '__main__':
    main()