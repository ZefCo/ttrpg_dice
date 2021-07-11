import dice_roller
import dice_roller as dr

class PlayerHand:
    def __init__(self) -> None:
        self.hand = {}

    def empty_hand(self, *args):
        for obj in args:
            try:
                for dice in vars(obj):
                    print(dice)
                    self.hand[dice] = 0
            except:
                print("obj does not have vars()")

    def roll_dice(self, throwdice):
        try:
            for dice, ammounts in throwdice.items():
                # print(dice, ammounts)
                pass
        except:
            print("Input objec was not a dictionary")

    # a way to add dice

def main():
    pass

if __name__ in '__main__':
    main()