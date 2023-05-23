Name: Jonathan Kim

2048!  A popular game that was implemented using pygame and numpy in Python!


Running Instructions:  It's a pretty straightfoward, just download the file, open it in any editor, and run the game.py file!  You should get a pygame pop-up for the 2048 game, assuming that python is installed and can be run.

Use the arrow keys to move the 2048 game up and down, left and right (depending on how you want the tiles to shift into your behavior).  The restart button if you lose is caused by the return/enter button, and escaping requires just X-ing out the window!

A link on how to play:  https://levelskip.com/puzzle/How-to-play-2048 


******************
**Code Structure**
******************


grid.py:  Stores my board class definition as well as various methods that handle the movements from the board and generations of new pieces.  Also had __str__ magic methods for debugging and initialization.  (One class definition/two dunder methods)

game.py: Stores the implementation of my game, and where the pygame magic happens!  Imports the Board class from board.py, and uses various drawing functions created within the game.py file to draw out the board and to handle various movement events, restart events, and exit event.  Uses a while loop to handle the constant playing of the game until a loss is found, and also stores the high score if it is beaten!  Run this file to run the game!


dictionary.py:  Stores the colors dictionary, which is a dictionary that has the value of the tile as keys and the rgb color index for the value of the dictionary.  Also has text colors of the numbers within each colored tile, the board color outside, and colors of tiles greater than 2048.  Put in this file so that both the board.py and game.py could access this dictionary by importing it!


high_score: a simple document that just stores the high score value.  It's just where I store the high score of all time, regardless of the instance of the 2048 game being played.
In the game file, I store this during the while loop.

In-line documentation and code style: each function should have proper documentation are found in the main.py file
