# ttrpg_dice

7/8/21

This project eveolved from wanting to learn Rust and starting with a way to make a dice roller for the Star Wars TTRPG by Fantasy Flight. It involved using a JSON file to store the dice information then pulling that into Rust, randomly generating a number, and comparing that to the JSON file. That's the short short description. Being that it was the first time I was using Rust this project actually is quite a bit more involved then just that, as Rust has some very interesting requirements and traits that boils down to accouting for everything.

Realizing that I had to know the right questions to ask, and being more comfortable in Python, I've decided to change my stragety: do it in Python first, find a good algorithm, and then take those ideas to Rust to learn how Rust works. In other words I'm going to learn more about Python to learn more about Rust. I'll try to use the README.md as a log of what I am doing and the alogirthm involved.


10/22/22

New stragety: use what I now know about random number generators to develop a C++ script that will generate the numbers, and lay that onto a UI. Will have to develop a lot more JSON files and figure out how to read them into C++, or combine Python and C++.