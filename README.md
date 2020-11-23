# Introduction

pgn-pruner takes a directory of a pgn or a pgn as plain text.

All the tags and comments are removed from the file to simplify and condense the file as much as possible.

It then asks the user to see how long you want the longest line in the pgn to be.
- It makes sure the user input is greater than 0 and an integer
    - If it is not it will ask the user to re enter a value
- It finds the longest line in the pgn.
- It then compares this to the user entered value.
    - If the user entered value is greater than the longest line, they are asked to re neter a value.
    - If the user entered value is less than the longest line, the progam continues.

The program the removes all lines which are longer than the user entered value and will either print the pgn as plain text or create a new file containing the pgn.