import os 
import sys

while True:
    path = int(input("Press 1 to past a pgn as plain text or press 2 to enter an address to a pgn\n"))
    if path == 1:
        pgn_text = input("Please past pgn here:\n")
        break
    elif path == 2:
        pgn_location = input("Enter location your pgn:\n")
        if os.path.exists(pgn_location):
            print(os.listdir(pgn_location))
            break
    


max_moves = input("How many moves would you like to prune too? ")