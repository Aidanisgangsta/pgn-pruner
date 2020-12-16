import ast

e1 = "( ( ) ( ) ) ( ( ) ( ( ) ) ) ( )"
e2 = "0(1(2)(3(4)5)(6)789)0"
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
        #Finds the location of all the close brackets
        elif item[-1] == ")":
            close_brackets.append(index)
            brackets.append(index)

    #Finds the bracket pairs
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
        """
        A function that sorts the nested brackets into nested lists.\n

        e.g. a(b(c)d) -> [a, [b, [c], d]]
        """

        for index, item in enumerate(lst):
            if any(index in tup for tup in tups):
                for pos1, pos2 in tups:
                    if index == pos1:
                        new_lst.append("[")
                    elif index == pos2:
                        new_lst.append("]")
            else:
                new_lst.append(item)

        print(new_lst)
        
        list_string = "".join(new_lst)
        print(list_string)

        print()

    create_list()

bracket_pairs(e2)