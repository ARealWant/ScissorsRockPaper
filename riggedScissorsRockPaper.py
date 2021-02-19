''' Why both modules are imported will be shown down below '''
import time

print("[👋]  Welcome to Scissors Rock Paper!"); time.sleep(1.5)
# We're welcoming the player and waiting 1.5 seconds ^ using the imported time module
figure  = ("Scissors", "Rock", "Paper") # All figure the player/computer can choose

game_status = True
while game_status is True: # Due to game_status will be True all the time, we're putting the process in a while loop

    # The player will choose their figur here
    player_choose = 0
    while player_choose not in(1,2,3):
         player_choose = int(input("\n[1] Scissors | [2] Rock | [3] Paper\n"))
         # Tip: \n is the standard newline character, which prints a new line after printing the opportunities to choose
    player_figur = figure[player_choose - 1]

    if player_figur == "Scissors":
        print("[❌]  Game lost! Computer selected: Rock")
    elif player_figur == "Rock":
        print("[❌]  Game lost! Computer selected: Paper")
    elif player_figur == "Paper":
        print("[❌]  Game lost! Computer selected: Scissors")

    # Waiting 2 seconds before asking for the restart
    time.sleep(2)

    choose_restart = "" # We're expecting a string, that's why we're defining it here
    while choose_restart.lower() not in ("y", "n", "yes", "no"): # We're using the builtin .lower() here, should the player send the letter in caps the input will be lowercase automatically
        # Tip: Should the player give us something else than "y" and "n", we'll show them the opportunities again = while loop
        # Tip: Don't forget that game_status is set to True already, due to that the game will start again
        choose_restart = input("\n[🔁]  Restart the game? [y] YES | [n] NO\n")
        time.sleep(2)

    if choose_restart == "n" or "no":
        print("\n[✋]  Alright! Game has been stopped, you can start it whenever you want again.\n")
        time.sleep(2)
        game_status = False # We'll stop the while loop with setting this to False, as mentioned above