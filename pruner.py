import os 
import sys
import sentence

def pgn_getter():
    while True:
        path = int(input("Press 1 to past a pgn as plain text or press 2 to enter an address to a pgn\n"))
        if path == 1:
            pgn_text = input("Please past pgn here:\n")
            break
        elif path == 2:
            pgn_location = input("Enter location your pgn:\n")
            #removes space from directory name
            remove_spaces(pgn_location)
            print(os.path.isfile(pgn_location))

            if os.path.isfile(pgn_location):
                print(os.listdir(pgn_location))
                break
    
def move_to_prune():
    max_moves = input("How many moves would you like to prune too? ")

"""
Used to remove all white space in the directory name just incase there is a space or spaces in the give directory
"""
def remove_spaces(dir):
    sentence.strip(dir)

def main():
    pgn_getter()
    move_to_prune()

main()