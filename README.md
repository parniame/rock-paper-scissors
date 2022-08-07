# rock, paper, scissors
I have created this simple, classic game.
It's an implementation of [rock, paper, scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors),that takes user input from the terminal and plays against The computer.  

## Instructions and Algorithm
This project includes several main functions(menu/sign_in/login/user_panel/game) that their explanation is in "How it works", besides the functions `Scoreboard` and `show_stats` are written for show the saved scores and the users scores respectively, also the functions(`empty_string`,`is_defined`,`is_correct`,`increase`) are written for having a clean and user friendly code.  

## Libraries
1. The data of users like username, wins, etc will be available after terminating the game, for this reason i used a csv file and for working with this file i used pandas from the python library.  
2. I defined an array for actions rock, paper, scissors and the user selects an element of this array by entering 1 or 2 or 3. The computer plays one round by choosing randomly an element of the array randomly, for this purpose, I used `NumPy` from the python library. 

## How it works
by running the project, the menu panel will print in the terminal 

### Menu
it asks for an integer number with this process as follows:
```
choose one number please(1/2/3/4 ?):
    1. Signin 2. Login 3. Scoreboard 4. Exit
```
every user can enter the user_panel with typing NO.1(`signin`) and NO.2(`login`), and also by typing NO.3(Scoreboard). The saved users with their scores are shown in the terminal, furthermore by typing NO.4 the project will be stopped.

### sign in
by typing NO.1(`signin`) in menu panel, sign_in panel will print in the terminal ,it asks for your name and then your username ,if the username was not used before, it would ask for a password for your username, after that you  enter to  user_panel.

### login
by typing NO.2(`login`) in menu panel,login panel will print in the terminal ,it asks for your username ,if the username was defined, it would ask for the password for your username, after that you enter to  user_panel.

### user panel
by entering the user_panel with login or signin, it will print in the terminal, it asks for an integer number as follows:

```
welcome to your account 
        please choose one number(1/2/3 ?)
        1.start a game 2.show your stats 3.logout 
```
by typing NO.1(`start a game`) ,game panel will print in the terminal, and NO.2(`show your stats`) will print your number of wins and losses and also the win rate ,and by typing NO.3(`logout`) you will go back to menu.

### Game panel
by typing NO.1(start a game) in `user_panel`, firstly you are asked of the score limit of the game
(Whenever any player reaches that score is the winner and the game is over). The score limit must be an integer otherwise the game panel will be run again.

```
please enter the  score limit of the game(integer)","""(Whenever any player 
    reaches that score is the winner and the
                game is over
```
now by starting the game, the project takes user input from the command line :
```
please choose one number(1/2/3 ?)
                1.rock, 2.paper, 3.scissor
```
it also must be an integer and in range 1,2,3 (otherwise the data of the game will be saved and it asks if you want to continue in order to run the game panel again or going back to user_panel), then The computer will choose a random choice between "Rock", "Paper" and "Scissor". The user will be wined or lost and it will be continued until a player reaches the score limit. after that this data will be saved and you will entered back to the user_panel.

### Install & Run
```
git clone https://github.com/parniame/rock-paper-scissors.git
cd rock-paper-scissors
chmod +x rock_paper_scissors.py
python3 -m venv .venv
pip3 install -r requirements.txt
python3 ./rock_paper_scissors.py
```
