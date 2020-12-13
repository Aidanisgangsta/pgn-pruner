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
