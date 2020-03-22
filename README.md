# kingsheep


# Programming a Kingsheep Agent (100%)
In the figure below, you can see how the GUI of the game looks like.
Each game is played by two players (P1 and P2)  that play against each other. A player has to operate two agents: the sheep and the wolf.
The wolf's objective is to sabotage the other player, by removing food items and trying to catch the opposite player's sheep. The sheep's objective is to score as many points as possible by eating food items.

## Rules and Objective of the Game
# Rules:
Both, the wolf and the sheep have 5 movement options for each call:

move = MOVE_DOWN; 
move = MOVE_UP;
move = MOVE_LEFT;
move = MOVE_RIGHT;
move = MOVE_NONE;
The wolf is allowed to make a step for every second step of the sheep. In other words the sheep can move twice as fast as the wolf. 

Wolves cannot step on squares occupied by the opponent’s wolf (wolves block each other).
Wolves cannot step on squares occupied by the sheep of the same player.
Sheep cannot step on squares occupied by the wolf of the same player.
Sheep cannot step on squares occupied by the opposite sheep.
Neither the sheep nor the wolf can enter a square with a fence on.
Neither the sheep nor the wolf can step on a square outside the map. Imagine the map is surrounded by fences.
If the sheep steps on a food object the food object is consumed (removed from the map) and a score is awarded.
If the wolf steps on a food object the food object gets removed but no score is awarded.
Each game lasts for a maximum of 100 turns or unless a sheep gets caught by the wolf, then the game ends immediately.
If the wolf of player1 catches the sheep of player2 the game ends immediately and player1 wins and is awarded all the points for the current run.

## Objectives:
# For the sheep:

Avoid the wolf of the opposite player.
Maximize points, by consuming as many food objects as possible.
The rhubarb object gives you five score points
The grass object gives you one score point
For the wolf:
Catch the other player's sheep.
Remove food objects to sabotage the other player.
Block the other wolf.
 

## Project Setup

The instructions below are for running the game and your code in the terminal. Alternatively, you can use an IDE of your choosing, e.g. PyCharm.

Open command prompt/terminal in the project root folder (containing the kingsheep.py file)
Activate the environment you created by running conda activate pai2020_a1
Call the game from the python file kingsheep.py. You have the following options:
-d: turns on debug mode and prints the state of the game after each iteration in the terminal. 
-v [int]:  determines the verbosity level, i.e. how much information is printed: 1 prints the elapsed time, 2 adds the system messages, 3 adds the final game state of the game. 
-g: turns on the graphics, so you can see the sheep and wolves walk around and follow the progress of the game visually. 
-s [float]: slows down each iteration in seconds when -g is set (fractions are allowed), making it easier for you to see how your agents behave. 
-p1m [string]: enter the name of the module of player 1 here.
-p1n [string]: enter the name of the class that defines player 1 here.
-p2m [string]: enter the name of the module of player 2 here.
-p2n [string]: enter the name of the class that defines player 2 here.
map [filepath/to/map.map]: the file path to the map you want to run the game with
So for example, if I want to run the map test.map which is in the folder resources, and I want the Random player (defined in the class RandomPlayer in the module random_player) to play against the greedy player (defined in the class GreedyPlayer in the module greedy_player), and I want graphics + debug information with a slowdown of 0.1 seconds, I would call the game using the following line:

python kingsheep.py resources/test.map -p1m random_player -p1n RandomPlayer -p2m greedy_player -p2n GreedyPlayer -d -g -s 0.1

Note that the player modules need to be in the same folder as the kingsheep.py file in the current setup. Also note that when you create new maps to test your agents on, they need to have the file format NAME.map (you can simply create them in a text editor, for example by editing the provided map). 

# Building your agents

The folder you receive contains the following:

config.py: sets the global variables such as field height.
kingsheep.py: runs the game and is the main file.
resources: contains test map and images needed for the graphical representation
4 preset players:
greedy_player.py: this agent uses a simply greedy approach
passive_player.py: this agent simply stays in place
random_player.py: this player makes a random move every turn
example_player.py: a blank template agent
You are given the example agent in example_player.py to get started. You need to do the following within this file (this instruction is also included in the file, and will make more sense once you open the file):

Change the name of your file to '[uzhshortname]_A1.py', where [uzhshortname] needs to be your uzh shortname.
Change the name of the class to a name of your choosing
Change the def 'get_class_name()' to return the new name of your class
Change the init of your class:
self.name can be an (anonymous) name of your choosing
self.uzh_shortname needs to be your UZH shortname
Update move_sheep and move_wolf
Your task is to develop an agent to play Kingsheep. We recommend implementing various versions and testing them against each other. That way, you see which agent performs best.

# Various Kings Sheep Maps

You can create different maps . To do this, copy test.map and edit the new file in a text editor.
The map consists of 15x19 squares and each square can contain one of four elements, represented by the following symbols:

Empty "."
Grass "g"
Rhubarb "r"
Fence "#"
The start position of the players are represented by the digits:

S (Sheep player 1)
W (Wolf player 1)
s (Sheep player 2)
w (Wolf player 2)
Change the symbols as you wish. You can not change the size of the map. All maps should have symbols distributed symmetrically.
Change the name of your map argument in your run configuration, to run the agents on your custom map. Feel free to share your maps on the forum. 

The maps used for the evaluation, will not be published, but they will stick to these restrictions.

# Write your first KingSheep-Agent

Open the example_player.py file. The main functions are move_sheep and move_wolf. Do NOT change the signature of these functions. Furthermore, both functions need to return one of the possible moves (MOVE_UP, MOVE_DOWN, MOVE_RIGHT, MOVE_LEFT, MOVE_NONE), followed by the p_state dictionary (again, do not change this otherwise the code will not run). It is up to you to figure out how to determine which moves your sheep and wolf should take. 

Both the move_sheep and move_wolf functions provide you 4 parameters:

p_num: player number (either 1 or 2) – this remains constant within one game and is determined by the p1m, p1n, p2m and p2n command line parameters
p_state: a dictionary which allows you to persist state between moves (e.g. to avoid having to parse the entire game field for each move). You cannot store state within the player class directly due to the use of multiprocessing. For example, to retain a counter for the number of moves, add the following lines to the top of the move_sheep or move_wolf functions:
if “counter” not in p_state:

     p_state[“counter”] = 1

else:

     p_state[“counter”] += 1

p_time_remaining: the number of seconds of computation time your players (sheep + wolf) have remaining.
field: a textual representation of the current game field
We recommend that you to build a search tree using the algorithms you have learned in the course so far. Based on that search tree, your implementation should assign a suited action. You are only allowed to use the modules included in the pai2020_A1 environment. Note that it has to be a search algorithm, not a learning algorithm, that you implement!

Your agents (sheep + wolf) have a combined maximum of 100 seconds of computation time per game. Since the game has a maximum of 100 iterations, this equates to an average of 1 second of computation time per move. As mentioned above, the remaining time can be accessed through the p_time_remaining argument. If your agent thinks too long, the game will stop, and the opponent will have won. In other words, make sure your code is not too computationally heavy.
