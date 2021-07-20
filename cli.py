import re


def dice_match(string_input, *args, **kwargs):

    dice_hold = {k:0 for k in args}

    dice2roll = re.findall(r'd?\w+=\d+', string_input)
    
    for chunk in dice2roll:

        key = re.search(r'(d\d+|\w+)', chunk)
        key = key.group()
        
        ammount = re.search(r'=\d+', chunk)
        ammount = int(re.sub(r'=', '', ammount.group()))
        
        dice_hold[key] = ammount

    return dice_hold

def rules_match(string_input):
    rules = re.match(r'roll(_\w+|!)', string_input)

    if rules:
        if re.search(r'!', rules.group()):
            return 'stand'

        elif re.search(r'_\w+', rules.group()):
            rules = re.sub(r'roll_', '', rules.group())
            return rules

def main():
    pass


if __name__ in '__main__':
    main()