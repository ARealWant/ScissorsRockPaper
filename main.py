import os
print("Choose between the Normal and Rigged version [n/r]:")

answer = input()

if answer.lower() == "r":
    print("Ok! Starting the Rigged Version...\n")
    os.system(".python3 riggedScissorsRockPaper.py")
else:
    print("Ok! Starting the Normal Version...\n")
    os.system("python3 ScissorsRockPaper.py")