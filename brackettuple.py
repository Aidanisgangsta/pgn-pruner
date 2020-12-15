e1 = "( ( ) ( ) ) ( ( ) ( ( ) ) ) ( )"
e2 = "0(1(2)(3(4)5)(6)7)"
e3 = "( ( ( ) ( ( ) ( ) ) ) ( ( ) ( ) ) )"

def bracket_pairs(ex):
    """
    A function that will find the pairs of brackets in the pgn.\n

    -Returns a list of tuples containing the pairs of array locations of the bracket pairs.
    """

    lst = []

    for char in ex:
        lst.append(char)
    
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
        elif item[-1] == ")":
            close_brackets.append(index)
            brackets.append(index)

    open_bracket = [] 
    for bracket in brackets:
        if bracket in open_brackets:            
            open_bracket.append(bracket)
        elif bracket in close_brackets:
            tups.append((open_bracket[-1], bracket))
            open_bracket.pop(-1)

    tups = sorted(tups, key=lambda tup: tup[0])

    new_lst = []

    def create_list():
        for index, item in enumerate(lst):
            if any(index in tup for tup in tups):
                for pos1, pos2 in tups:
                    if index == pos1:
                        new_lst.append([])
                    elif index == pos2:
                        new_lst.append([])
            else:
                new_lst.append(item)

    create_list()
    print(new_lst)

bracket_pairs(e2)