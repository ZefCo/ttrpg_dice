# ttrpg_dice

7/8/21

FROM MAIN README
This project eveolved from wanting to learn Rust and starting with a way to make a dice roller for the Star Wars TTRPG by Fantasy Flight. It involved using a JSON file to store the dice information then pulling that into Rust, randomly generating a number, and comparing that to the JSON file. That's the short short description. Being that it was the first time I was using Rust this project actually is quite a bit more involved then just that, as Rust has some very interesting requirements and traits that boils down to accouting for everything.

Realizing that I had to know the right questions to ask, and being more comfortable in Python, I've decided to change my stragety: do it in Python first, find a good algorithm, and then take those ideas to Rust to learn how Rust works. In other words I'm going to learn more about Python to learn more about Rust. I'll try to use the README.md as a log of what I am doing and the alogirthm involved.

7/8/21

PYTHON
For the Python script the goal is to make a script that can be used for any possible wild and wierd set of dice. This means that I want to use closures, first class fucntions, and decorators. I want to make a script that can, with a little tweeking, turn into a dice roller for any rpg that uses unique dice, or be useful for any regular rpg using standard dice.

The ultimate goal for this would be to make a personal dice roller for discord, or an executable with a nice 8/16 bit art style GUI.