# ttrpg_dice

7/20/21

How to do the cli: I don't want to write seperate scripst for each dice roller: I just want one and you can access all of them from the main. So when sending a command I want the user to tell the script everything it needs. I'll need a "help" script in the end. Until then let's come up with a standard for commands to tell the thing what to do.

roll_rules!(dice=ammount)

So it would be r'roll_\w+!((\d+|\w+)=\d+)' or something.

The main challenge however is how to access the rulesets: 1) do I want to do this, 2) how do I do this? For 1: the main problem is that I have to write a script every time I want to add a thing, but that is tedious. For 2, it's rather complicated right? So instead I should store a lot of the data in JSON files, and just come up with a scheme that allows me to use the JSON files for manipulation. That way if I want to add information I can just append the JSON file folder and I'm done.

7/19/21

This is probably pretty complicated and dumb.

How about this: I roll a dice with x number of sides. I figure out what that number is. Then I compare it to a list with the results and print those results.

We'll start with standard dice.

What I want is for the user to be able to do something like roll!(dice1=#, dice2=#, dice3=#) and it give them the result. So kwargs is the route to go.

7/10/21

New goal: instead of initializing things seperatly, let's create a Dice Bag that pulls pulls the json data and then creates the dice objects and stores those objects. So an object to create and store other objects.

Then create another object, the players hand, which holds - by default - 0 of each dice. We can then increse the number of each dice in the hand and roll those. The player hand only needs to be initizalized when needed.

CURRENT ALGORITHM

Right now it's a giant mess because I can't quite decide the best approach to this. Should I use more classes? Should I use less?

Use a Dice as an object.

Should the dice bag be an object?

Probably not: that's probably me doing extra steps for no gain. Should probably just create the handful of dice when needed and pull the data of the dice when I create the handful.

-dice_roller.py rolls the dice. 
-random_generator(low, high, iterations=1) generates an iterations length tuple of random numbers between high and low and returns that. 
-file_importer.py is a genereic file importer (useful for the future)
-dice_class.py creates the class for the dice. Current attributes are high score, low score, and results (meant to future proof for other games that use none standard dice)
-dice_bag.py creates the dice pools to be used (?)

7/8/21

FROM MAIN README
This project eveolved from wanting to learn Rust and starting with a way to make a dice roller for the Star Wars TTRPG by Fantasy Flight. It involved using a JSON file to store the dice information then pulling that into Rust, randomly generating a number, and comparing that to the JSON file. That's the short short description. Being that it was the first time I was using Rust this project actually is quite a bit more involved then just that, as Rust has some very interesting requirements and traits that boils down to accouting for everything.

Realizing that I had to know the right questions to ask, and being more comfortable in Python, I've decided to change my stragety: do it in Python first, find a good algorithm, and then take those ideas to Rust to learn how Rust works. In other words I'm going to learn more about Python to learn more about Rust. I'll try to use the README.md as a log of what I am doing and the alogirthm involved.

7/8/21

PYTHON
For the Python script the goal is to make a script that can be used for any possible wild and wierd set of dice. This means that I want to use closures, first class fucntions, and decorators. I want to make a script that can, with a little tweeking, turn into a dice roller for any rpg that uses unique dice, or be useful for any regular rpg using standard dice.

The ultimate goal for this would be to make a personal dice roller for discord, or an executable with a nice 8/16 bit art style GUI.