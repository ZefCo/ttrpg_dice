import dice_roller as dr
import dice_class as dc
import file_importer as fi
import dice_bag as db
import os
import handful_of_dice as hod

def main():
    # pass
    cwd = os.getcwd()
    standard_dice_path = os.path.join(cwd, 'JSONS', 'standard_dice.json')
    dicebag = db.DiceBag()
    dicebag.load_data_from_json(standard_dice_path)
    hand = hod.PlayerHand()
    hand.empty_hand(dicebag)
    # print(hand.hand)

if __name__ in '__main__':
    main()