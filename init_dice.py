import os
import common_methods as cm
import dice_class as dc

def initialize_dice(dice_file):
    cwd = os.getcwd()
    standard_dice_path = os.path.join(cwd, 'JSONS', dice_file)
    json = cm.load_json(standard_dice_path)
    standard_dice = {k:dc.Dice(k, v['low'], v['high'], v['results']) for (k, v) in json.items()}

    return standard_dice


def main():
    pass


if __name__ in '__main__':
    main()