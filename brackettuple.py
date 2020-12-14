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
    tups = []    

    for index, item in enumerate(lst):
        #Finds the location of all the open brackets
        if item[:1] == "(":
            open_brackets.append(index)
            brackets.append(index)
        #Fidns the location of all the close brackets
        elif item[:1] == ")":
            close_brackets.append(index)
            brackets.append(index)

    print(brackets)

    open_bracket =[]
    for bracket in brackets:
        if bracket in open_brackets:            
            open_bracket.append(bracket)
        elif bracket in close_brackets:
            tups.append((open_bracket[-1], bracket))
            open_bracket.pop(-1)

    print(tups)

bracket_pairs(e2)