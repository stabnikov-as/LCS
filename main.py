
import lcs
import transformation as tr

X = 'CATCGA'
Y = 'GTACCGTCA'
# X = 'popa'
# Y = 'sholpya'

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

#find_and_print_lcs(X, Y)

operations = ['copy', 'rep', 'del', 'ins']
costs = [-1, 1, 2, 2]

X = 'ACAAGC'
Y = 'CCGT'

cost, op = tr.compute_transformation_table(X, Y, costs)

tr.print_transformation_table(cost, op, X, Y, operations)