import dice_roller as dr
import dice_class as dc
import file_importer as fi
import os

# class DiceBag:
#     def __init__(self, file_path) -> None:
#         self.pull_dice_from_file(file_path)

#     def initialize_dice_bag(self, func):
#         def wrapper(*args, **kwargs):
#             self.bag = {}
#             j = func(*args, **kwargs)
#             for dice, attributes, in j.json_data.items():
#                 temp = dc.Dice(dice, attributes['low'], attributes['high'], attributes['results'])
#                 self.bag[temp.name] = temp
        
#         return wrapper

#     @initialize_dice_bag
#     def pull_dice_from_file(self, file_path):
#         j = fi.File(file_path)
#         j.load_json(j.file_path)

def dice_bag(func):
    def wrapper(*args, **kwargs):
        bag = {}
        j = func(*args, **kwargs)
        for dice, attributes in j.json_data.items():
            temp = dc.Dice(dice, attributes['low'], attributes['high'], attributes['results'])
            bag[temp.name] = temp
        
        return bag
    return wrapper

@dice_bag
def grab_dice(file_path):
    j = fi.File(file_path)
    j.load_json(j.file_path)

    return j


def main():
    pass

if __name__ == '__main__':
    main()
