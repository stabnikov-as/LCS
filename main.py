
import lcs
import transformation as tr


def find_and_print_lcs(X, Y):
    '''
    :param X: string, first  word
    :param Y: string, second word
    :return: LCS, string
    '''
    # Find LCS table - a table containing lengths of longest common substrings of Xi and Yj
    l = lcs.compute_lcs_table(X, Y)
    # Print the found table
    lcs.print_lcs_table(l, X, Y)
    # Assemble lcs using words and table
    LCS = lcs.assemble_lcs(X, Y, l)
    print('\nLCS = ' + LCS)
    return LCS

def transform_strings(X, Y, costs, operations):
    '''
    A function to transform one string to another
    :param X: str, first work
    :param Y: str, second word
    :param cost: list of ints, cost of operations
    :param operations: list of strings, the names of operations
    :return: nothing
    '''

    # assemble transformation and operations tables
    cost, op = tr.compute_transformation_table(X, Y, costs)
    # Print the found table
    tr.print_transformation_table(cost, op, X, Y, operations)
    # Assemble the transformation
    # This doesn't really do anything
    # Since we already know what the transformed string is
    tr.assemble_transformation(X, Y, op)

X = 'CATCGA'
Y = 'GTACCGTCA'

#find_and_print_lcs(X, Y)

X = 'ACAAGC'
Y = 'CCGT'

operations = ['copy', 'rep', 'del', 'ins']
costs = [-1, 1, 2, 2]

#transform_strings(X, Y, costs, operations)





