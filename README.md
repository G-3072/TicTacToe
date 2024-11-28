# TicTacToe


## Introduction
This project was made for the school subject "Berufsübergreifende Projekte".

My goal for this project was to create a TicTacToe with a computer opponent using Python.  
The Key features of my project are:

- A Graphical User Interface (GUI)
- A start menu with an option to select the game mode or exit the game
- A multiplayer mode for playing against other people
- A singleplayer mode with a computer opponent
- An end menu with options to rematch, change game modes, or quit the game

to create the game and GUI of the project i used the Pygame and Numpy libraries. Pygame was used to simplify the graphics and user inputs. Numpy was used so for speed since numpy arrays are faster than standard arrays

For my computer opponent i used a minimax algorithm so it selects the best possible moves. minimax is a decision making algorithm used mostly in turn based games. 

Here are links that helped me understand minimax:

https://www.youtube.com/watch?v=5y2a0Zhgq0U  
https://www.neverstopbuilding.com/blog/minimax  
in this video only until 6:20: https://www.youtube.com/watch?v=l-hh51ncgDI&t=197s 

## How to use
### How to install 
This project is written in python 3.12.3 so you need python 3.12.3 installed on your device. if you dont have Python you can download it here: 
https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe
  
if you have python installed these are the steps to install the project:  

1. clone the git repository: `git clone https://github.com/G-3072/tictactoe.git`

2. open project directory: `cd tictactoe`

3. install libraries: `pip install -r requirements.txt `


### How to start

To play the game in the `tictactoe` directory run: `python main.py` and the game will start. 

### How to close

the game can be closed at any time with the "X" at the top right of the window. there are also quit buttons in the start- and stop menus of the game taht close the game.

## Open features

in the curret state the project acomplishes all its goals. But there are still some flaws that could be improved or features that could be added. these are:  


- More efficient minimax implementation.
    - the current algrithm picks the correct move and i haven't been able to beat it but on the first move it has to make it takes ca. 4s to make the move. This is because it has to simulate ca. 40'000 different positions. 
    This could be improved with a more efficient algorithm or just storing the first moves so it dont has to calculate them every time.

