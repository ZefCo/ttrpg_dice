import dice_roller as dr
import dice_class as dc
import os
import common_methods as cm
import init_dice
import standard_roller as stand
import inspect
import swrpg_roller as swrpg

def main():

    # standard = stand.roller
    # cli = stand.cli

    starwars = swrpg.roller
    cli = swrpg.cli

    cli()


if __name__ in '__main__':
    main()