import os 
import sys

def pgn_getter():
    """
    A function which prompts the user to either paste a pgn as text or to enter the directory of a pgn file.\n

    The user first selects whether to paste the pgn as text or to enter the directory location of the file.
    The user is then prompted to either enter the text or directory location.
     - If they enter a directory, it is passed through a the remove_spaces function to remove all spaces from the directory name.
      - The file is then retrieved and the pgn converted into plain text where it is stored under a variable.
     - If the enter a pgn as text, it is stored under a variable.
    """

    while True:
        path = int(input("Press 1 to past a pgn as plain text or press 2 to enter an address to a pgn\n"))
        if path == 1:
            pgn_text = input("Please past pgn here:\n")
            break
        elif path == 2:
            raw_pgn_location = input("Enter location your pgn:\n")
            #Removes space from directory name
            pgn_location = remove_spaces(raw_pgn_location)

            if os.path.isfile(pgn_location) == True:
                with open(raw_pgn_location) as pgn:
                    print(pgn)
                break
  
def move_to_prune():
    """
    A function that prunes a pgn to a user defined number of moves.\n

    Will find the longest branch in the pgn and compare it to the user defined length they wish to prune to.
    If the lognest branch is shorter than the user difined value, they are asked to enter a smaller number.
    Provided that the user input is positive, non 0 and an iteger, the program will then continue.
    """

    max_moves = input("How many moves would you like to prune too? ")

def remove_spaces(dir: str) -> str:
    """
    A simple function which removes all spaces in a give directory.\n

    This is so the directory name given is accurate and can be found by the program.
    """

    #Removes all white space
    stripped = dir.strip()
    
    return stripped

def main():
    pgn_getter()
    move_to_prune()

main()