import os 
from chess import pgn
import re
import keyboard

def pgn_getter() -> str:
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
            print("Paste your pgn here:")
            #Creates a list of all the lines in the pgn
            while True:
                line = input()
                pgn_lines.append(line)
                #When the user presses enter the loop breaks
                if keyboard.is_pressed('enter'):
                    break
            #Joins the list of all the lines of the pgn to creates a single string
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
                    #Converts pgn to type string
                    pgn_text = str(pgn_text)
                break

    return pgn_text

def remove_spaces(pgn_dir: str) -> str:
    """
    A simple function which removes all spaces in a given directory name.\n

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

def clean_pgn(pgn: str) -> str:
    """
    A function which cleans the pgn of all unnecessary data.\n

    Removes:
     - Comments
     - Tags
    """

    def remove_comments():
        """
        A function which removes all comments from the pgn.\n

        Removes all data between curly brackets { }.
        """

        removed_comments = re.sub(r"\{((.|\n)*?)\}", "", pgn)

        return removed_comments

    def remove_tags():
        """
        A function which removes all tags from the pgn.\n

        Removes all data between square brackets [ ].
        """

        removed_tags = re.sub(r"\[((.|\n)*?)\]", "", pgn)

        return removed_tags

    def remove_line_breaks():
        """
        A function that removes all line breaks from remoing the comments.\n

        Removes all line breaks to a blank character ("").
        """

        #Removes all line breaks (provided there is 4 or less)
        # TODO Convert to loop
        r1 = pgn.replace("\n", "")
        r2 = r1.replace("\n", "")
        r3 = r2.replace("\n", "")
        removed_line_breaks = r3.replace("\n", "")
            
        return removed_line_breaks

    pgn = remove_comments()
    pgn = remove_tags()
    pgn = remove_line_breaks()

    return pgn

def moves_to_prune(pgn: str) -> int:
    """
    A function that prunes a pgn to a user defined number of moves.\n

    Uses the value from longest_move and compares to the user entered value.
    If the longest branch is shorter than the user difined value, they are asked to enter a smaller number.
    Provided that the user input is positive, non 0 and an iteger, the program will then continue.
    """

    def longest_move() -> int:
        """
        A function which finds the longest line in the pgn.

        Finds the longest branch in the pgn by removing all non integer values and convering the remaining values into a list.
        """

        #Creates a list of all move numbers in the pgn
        moves = re.findall(r'\d+\.', pgn)
        #Creates a list of just the numbers (removes fullstops)
        integers = [int(x[:-1]) for x in moves]

        longest_line = max(integers)

        return longest_line

    longest_line = longest_move()

    while True:
        max_moves = input("\nHow many moves would you like to prune to? ")
        if is_int(max_moves) == True:
            if int(max_moves) > 0: 
                if int(max_moves) < longest_line:
                    break
                else:
                    print(f"Please pick a number that is less than {longest_line}")    
            else:
                print("Please enter and integer that is greater than 0")
        else:
            print("Please enter an integer")

    return max_moves

def pruner(pgn: str, prune_num: int):
    """
    The function that prunes a pgn to the user defined number of moves.\n

    Will find the longest branch in the pgn and compare it to the user defined length they wish to prune to.
    If the longest branch is shorter than the user difined value, they are asked to enter a smaller number.
    Provided that the user input is positive, non 0 and an iteger, the program will then continue.
    """

    pgn_split = pgn.split(" ")
    print(pgn_split)

def is_int(s: str) -> bool:
    """
    A simple function used to check whether a string is an integer.\n

    Will return true if the string is an integer, false otherwise.
    """

    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    pgn_text = pgn_getter()
    pgn_text = clean_pgn(pgn_text)
    prune_number = moves_to_prune(pgn_text)
    shortened_pgn = pruner(pgn_text, prune_number)

main()

# ?Useful regex statements
#[1-9][0-9]{0,2}\.
#\(.*?\)|(\S{1,7})