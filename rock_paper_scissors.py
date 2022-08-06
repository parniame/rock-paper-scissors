#!/usr/bin/python3
import pandas as pd
import numpy as np

df = pd.read_csv("dataset1.csv")

def menu(df):
    try:
        menu_in = int(input(''' welcome to Menu
    choose one number please(1/2/3/4 ?):
    1. Signup 2. Login 3. Scoreboard 4. Exit'''))
    except:
        print("the input is not an integer please try again!")
        menu(df)
    else:
        if menu_in == 1:
            sign_in(df)
        elif menu_in == 2:
            login(df)
        elif menu_in == 3:
            Scoreboard(df)
        elif menu_in == 4:
            print("You are exiting!")
            exit()

        else:
            print("the number is invalid please try again!")
            menu(df)

def sign_in(df):
    name = input(''' please enter your name''')
    empty_string(name)

    user_name = input("please enter a username")
    empty_string(user_name)

    if is_defined(df, user_name):
        print("this user name is already chosen  please choose another ")
        yes_no = input("do you want to continue(y/n)?")
        if yes_no.lower() != "y":
            menu(df)

        sign_in(df)
    else:
        password = input("please enter a password for your username")
        empty_string(password)

        df = df.append(
            {'name': name, 'username': user_name, ' password': password, 'wins': 0, '  losses': 0, ' win rate': 0.0},
            ignore_index=True)
        df.to_csv("dataset1.csv", index=False)
        index = int(df[df["username"] == user_name].index.values)

        user_panel(df, index)

def login(df):
    user_name = input("please enter your username")
    if is_defined(df, user_name):
        password = input("please enter your password for your username")
        index = int(df[df["username"] == user_name].index.values)
        if is_correct(df, index, password):
            user_panel(df, index)

        else:
            print("this password is incorrect")
            yes_no = input("\ndo you want to try again(y/n)?")
            if yes_no.lower() != "y":
                menu(df)

            login(df)

    else:
        print("this username is not defined")
        yes_no = input("\ndo you want to try again(y/n)?")
        if yes_no.lower() != "y":
            menu(df)
        login(df)

def Scoreboard(df):
    print(df[["username", "wins", "  losses", " win rate"]])
    menu(df)

def empty_string(str):
    if str.isspace() | (len(str) == 0):
        print("invalid string !")
        yes_no = input("do you want to continue(y/n)?")
        if yes_no.lower() != "y":
            menu(df)

        sign_in(df)

def is_defined(df, user_name):
    if user_name in df["username"].unique():
        return True
    return False

def is_correct(df, index, password):
    if password in df[" password"][index]:
        return True
    return False

def user_panel(df, index):
    try:
        user_in = int(input("""welcome to your account
        please choose one number(1/2/3 ?)
        1.start a game 2.show your stats 3.logout"""))
    except:
        print("the input is not an integer please try again!")
        user_panel(df, index)
    else:
        if user_in == 1:
            print("hi")
            game(df, index)
        elif user_in == 2:
            show_stats(df, index)
        elif user_in == 3:
            menu(df)
        else:
            print("the number is invalid please try again")
            user_panel(df, index)

def game(df, index):
    count_wins = 0
    count_losses = 0
    try:
        limit = int(input("please enter the  score limit of the game(integer)" + """(Whenever any player
    reaches that score is the winner and the
                game is over)"""))
    except:
        print("the input is not an integer please try again!")

        game(df, index)
    else:
        while True:
            print(count_losses, count_wins)
            if (count_losses == limit) | (count_wins == limit):
                break
            state = np.array(["rock", "paper", "scissors"])
            try:
                user_num = int(input("""please choose one number(1/2/3 ?)
                1.rock, 2.paper, 3.scissors"""))
            except:
                print("the input is not an integr please try again!")
                game(df, index)

            if (user_num > 3) and (user_num < 1):
                print("the number is invalid please try again")
                game(df, index)

            computer_num = np.random.choice(state)

            print("\n You chose  %s and computer chose  %s" % (state[user_num - 1], computer_num))

            if computer_num == state[user_num - 1]:
                print("Both chose %s ..It`s a tie!" % (computer_num))

            elif state[user_num - 1] == "rock":
                if computer_num == "paper":
                    print("Paper covers rock! You lose!")
                    count_losses += 1
                else:
                    print("Rock smashes scissors! You win!")
                    count_wins += 1


            elif state[user_num - 1] == "paper":
                if computer_num == "rock":
                    print("Paper covers rock! You win!")
                    count_wins += 1
                else:
                    print("Scissors cuts paper! You lose.")
                    count_losses += 1


            elif state[user_num - 1] == "scissors":
                if computer_num == "rock":
                    print("Rock smashes scissors! You lose.")
                    count_losses += 1

                else:
                    print("Scissors cuts paper! You win!")
                    count_wins += 1

    increase(df, index, count_wins, count_losses)
    user_panel(df, index)

def show_stats(df, index):
    print(df.loc[index][["wins", "  losses", " win rate"]])
    user_panel(df, index)

def increase(df, index, win, lose):
    df["  losses"][index] += lose
    df["wins"][index] += win
    df[" win rate"][index] = (df["wins"][index] / df["  losses"][index]) * 100
    df.to_csv("dataset1.csv", index=False)

menu(df)
