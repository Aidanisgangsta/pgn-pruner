e1 = "( ( ) ( ) ) ( ( ) ( ( ) ) ) ( )"
e2 = "(()(())())"
e3 = "( ( ( ) ( ( ) ( ) ) ) ( ( ) ( ) ) )"

def bracket_pairs(ex):
    """
    A function that will find the pairs of brackets in the pgn.\n

    -Returns a list of tuples containing the pairs of array locations of the bracket pairs.
    """

    lst = []

    for bracket in ex:
        lst.append(bracket)
    
    open_brackets = []
    close_brackets = []
    brackets = []

    for index, item in enumerate(lst):
        #Finds the location of all the open brackets
        if item[:1] == "(":
            open_brackets.append(index)
            brackets.append(index)
        #Fidns the location of all the close brackets
        elif item[:1] == ")":
            close_brackets.append(index)
            brackets.append(index)


    for index in brackets:
        if index in open_brackets:
            pass
        elif index in close_brackets:
            pass

bracket_pairs(e2)