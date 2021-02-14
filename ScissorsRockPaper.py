''' Why both modules are imported will be shown down below '''
import random
import time

print("[👋]  Welcome to Scissors Rock Paper!"); time.sleep(1.5)
# We're welcoming the player and waiting 1.5 seconds ^ using the imported time module
figure  = ("Scissors", "Rock", "Paper") # All figure the player/computer can choose



game_status = True
while game_status is True: # Due to game_status will be True all the time, we're putting the process in the while loop

    # The player will choose their figur here
    player_choose = 0
    while player_choose not in(1,2,3):
         player_choose = int(input("\n[1] Scissors | [2] Rock | [3] Paper\n"))
         # Tip: \n is the standard newline character, which prints a new line after printing the opportunities to choose
    player_figur = figure[player_choose - 1]

    # Figur the computer will choose randomly, for this process we're going to use our already imported random
    computer_figur = figure[random.randint(0, 2)] # Tip: Not "0,3" because you start count at zero in Python

    if player_figur == computer_figur:
        print("[⏳]  Tie game! Computer also selected " + computer_figur)
        # We're adding the randomly chose figur to the string here, no matter who won, this will show us what the computer chose
    else:
        if(player_figur == "Scissors"):
            if computer_figur == "Rock":
                print("[❌]  Game lost! Computer selected: " + computer_figur) # Player lost, Scissors lose against rock
            else: # We're using else here, because we're sure they is only one other possibility the player can win: Paper
                print("[✔]  Game won! Computer selected: " + computer_figur)

        if(player_figur == "Rock"):
            if computer_figur == "Scissors":
                print("[✔]  Game won! Computer selected: " + computer_figur)
            else:
                print("[❌]  Game lost! Computer selected: " + computer_figur)

        if(player_figur == "Paper"):
            if computer_figur == "Scissors":
                print("[❌]  Game lost! Computer selected: " + computer_figur)

            else:
                print("[✔]  Game won! Computer selected: " + computer_figur)



    # Waiting 2 seconds before asking for the restart
    time.sleep(2)



    choose_restart = "" # We're expecting a string, that's why we're defining it here
    while choose_restart.lower() not in ("y", "n"): # We're using the builtin .lower() here, should the player send the letter in caps the input will be lowercase automatically
        # Tip: Should the player give us something else than "y" and "n", we'll show them the opportunities again = while loop
        # Tip: Don't forget that game_status is set to True already, due to that the game will start again
        choose_restart = input("\n[🔁]  Restart the game? [y] YES | [n] NO\n")
        time.sleep(2)

    if choose_restart == "n":
        print("\n[✋]  Alright! Game has been stopped, you can start it whenever you want again.\n")
        time.sleep(5)
        game_status = False # We'll stop the while loop with setting this to False, as mentioned above