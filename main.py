
import util

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
    l = util.compute_lcs_table(X,Y)
    # Print the found table
    util.print_table(l, X, Y)
    # Assemble lcs using words and table
    lcs = util.assemble_lcs(X, Y, l)
    print('\nLCS = ' + lcs)
    return lcs

find_and_print_lcs(X, Y)