import os 
import sys
from chess import pgn
import re
import keyboard

def pgn_getter():
    """
    A function which prompts the user to either paste a pgn as text or to enter the directory of a pgn file.\n

    The user first selects whether to paste the pgn as text or to enter the directory location of the file.
    The user is then prompted to either enter the text or directory location.
     - If they enter a directory, it is passed through a the remove_spaces function to remove all spaces from the directory name.
      - The file is then retrieved and the pgn converted into plain text where it is stored under a variable.
     - If the enter a pgn as text, it is stored under a variable.
    """

    pgn_lines = []

    while True:
        path = int(input("Press 1 to past a pgn as plain text or press 2 to enter an address to a pgn\n"))
        if path == 1:
            print("Paste you pgn here:")
            #Creates a list of all the lines in the pgn
            while True:
                line = input()
                pgn_lines.append(line)
                #When the user presses enter the loop breaks
                if keyboard.is_pressed('enter'):
                    break
                #Joines the list of all the lines of the pgn to creates a single string
            pgn_text = " ".join(pgn_lines)
            break

        elif path == 2:
            raw_pgn_location = input("Enter the location to your pgn:\n")
            #Removes space from directory name
            pgn_location = remove_spaces(raw_pgn_location)

            if os.path.isfile(pgn_location) == True:
                #Opens pgn and reads as text
                with open(pgn_location, "r") as pf:
                    pgn_text = pgn.read_game(pf)
                    print(pgn_text)
                break
    return pgn_text
  
def moves_to_prune() -> int:
    """
    A function that prunes a pgn to a user defined number of moves.\n

    Finds the longest branch in the pgn and compares it the the user entered value.
    If the longest branch is shorter than the user difined value, they are asked to enter a smaller number.
    Provided that the user input is positive, non 0 and an iteger, the program will then continue.
    """

    while True:
        max_moves = int(input("How many moves would you like to prune to? "))
        if max_moves > 0:
            if type(max_moves) == int:
                break
            else:
                print("Please enter an integer\n")
        else:
            print("Please entere and integer that is greater than 0\n")

    return max_moves

def remove_spaces(pgn_dir: str) -> str:
    """
    A simple function which removes all spaces in a give directory.\n

    This is so the directory name given is accurate and can be found by the program.
    """

    dir_chars = []

    #Converts the directory into a list
    for i in range(len(pgn_dir)):
        dir_chars.append(pgn_dir[i])

    #Checks whether the the first character is blank or if any characters are spaces 
    if dir_chars[0] == '\u202a':
        dir_chars.pop(0)

    #Joins all characters in the array 
    stripped = "".join(dir_chars)

    return stripped

def clean_pgn(pgn):
    """
    A function which cleans the pgn of all unnecessary data.\n

    Removes:
     - Comments
     - Tags
    """
    def remove_comments():
        """
        A function which removes all comments from the pgn.\n

        Removes all data between curly brackets { }
        """

        removed_comments = re.sub(r"\s*{.*}\s*", " ", pgn)

        print(removed_comments)

    def remove_tage():
        pass

def pruner():
    """
    The function that prunes a pgn to the user defined number of moves.\n

    Will find the longest branch in the pgn and compare it to the user defined length they wish to prune to.
    If the longest branch is shorter than the user difined value, they are asked to enter a smaller number.
    Provided that the user input is positive, non 0 and an iteger, the program will then continue.
    """

def main():
    pgn_text = pgn_getter()
    max_moves = moves_to_prune()
    pgn_text = clean_pgn(pgn_text)

main()