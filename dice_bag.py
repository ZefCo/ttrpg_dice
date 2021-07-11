import dice_roller as dr
import dice_class as dc
import file_importer as fi
import os

class DiceBag:
    def __init__(self) -> None:
        pass

    def bag_from_dict(self, dictionary):
        for dice, attributes in dictionary.items():
            setattr(self, dice, attributes)

    def load_data_from_json(self, file_path):
        j = fi.File(file_path)
        j.load_json(j.file_path)
        for dice, attributes in j.json_data.items():
            temp = dc.Dice(dice, attributes['low'], attributes['high'], attributes['results'])
            setattr(self, dice, temp)

def main():
    cwd = os.getcwd()
    filepath = os.path.join(cwd, 'JSONS', 'standard_dice.json')
    dicebag = DiceBag()
    dicebag.load_data_from_json(filepath)
    # print(vars(dicebag))
    # for value in vars(dicebag):
    #     print(value)

if __name__ == '__main__':
    main()
