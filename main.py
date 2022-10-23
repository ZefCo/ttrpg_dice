import dice_roller as dr
import dice_class as dc
import os
import common_methods as cm
import init_dice
import standard_roller as stand
import inspect
import swrpg_roller as swrpg
import cli


def main():

    cwd = cm.cwd()
    rule_path = os.path.join(cwd, 'JSONS', 'rules.json')
    rulesNdice = cm.load_json(rule_path)

    # command_input = 'roll_swrpg(b=1, s=2, a=3, d=4, p=5, c=6, f=7)'
    command_input = 'roll!(d4=1, d6=2, d8=3, d10=4, d12=5, d20=6)'
    
    rules = cli.rules_match(command_input)

    dice = rulesNdice[rules]

    dice_roll = cli.dice_match(command_input, *dice)


if __name__ in '__main__':
    main()