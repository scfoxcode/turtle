# turtle
Basic program to draw lines in python3 using pygame

## Setup
1. Make sure you have python 3 installed on your system, this might be aliased by python or python3 in terminal, depending on your setup. You can check what version you have with `python --version` or `python3 --version` respectively.
2. Install the dependencies, primarily pygame, using the command `pip install -r requirements.txt` from the root directory of the project.
3. Run the programming using the command `python src/main.py` from the project root directory.

## Tasks
1. Change the colour of the lines
2. Modify the code so that the final 'o' is one grid square to the left of it's currrent position
3. We have a few places where we call bob.Right or bob.Left twice in a row. Add a Turn180 function to the turtle class
4. Add, Remove or update the Turtle's function calls to write your own name with lines
5. Modify the colour logic so that the line colour alternates from red to blue with each movement of the turtle (movement, not rotation)
6. All this turtle code in the main method is a bit cumbersome. Maybe split out each letter into it's own function, and call those from the main method
7. Go wild. Add whatever you want
